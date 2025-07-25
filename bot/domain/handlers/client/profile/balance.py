from aiogram import Bot, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from bot.data.repository.invoices import InvoiceRepository
from bot.data.whitepay import WhitePayRepository
from bot.domain.notification.NotificationAdmin import NotificationAdmin
from bot.domain.states.client.profile.BalanceState import BalanceState
from bot.presentation.keyboards.client.profile.kb_balance import (
    BalanceReplenish,
    kb_pay_invoice,
)

router = Router()


@router.callback_query(BalanceReplenish.filter())
async def balance_sum(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(BalanceState.Sum)
    await callback.message.answer(i18n.CLIENT.BALANCE_SUM())


@router.message(BalanceState.Sum)
async def balance_pay_invoice(message: types.Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    try:
        num = float(message.text)
        if not (5 <= num <= 10000000):
            raise ValueError
    except Exception as _:
        await message.answer(i18n.CLIENT.BALANCE_SUM_ERROR())
        return

    await state.clear()

    invoice_sum_with_procent = num + (num * 0.011)

    invoice_response = WhitePayRepository().create_invoice(sum_invoice=invoice_sum_with_procent)
    if not invoice_response:
        await message.answer(i18n.CLIENT.BALANCE_CREATE_INVOICE_ERROR())
        return

    # add transaction invoice to database
    if not InvoiceRepository().add(
        invoice_response["order"]["id"],
        invoice_response["order"]["order_number"],
        num,
        invoice_response["order"]["value"],
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name,
        invoice_response["order"]["created_at"],
    ):
        await message.answer(i18n.CLIENT.BALANCE_CREATE_INVOICE_ERROR())
        return

    await message.answer(
        i18n.CLIENT.BALANCE_INFO(
            id=invoice_response["order"]["id"],
            sum=invoice_response["order"]["value"],
            created_at=invoice_response["order"]["created_at"],
        ),
        reply_markup=kb_pay_invoice(invoice_response["order"]["acquiring_url"]),
    )

    await NotificationAdmin.invoice_init(invoice_response["order"]["id"], bot, i18n)
