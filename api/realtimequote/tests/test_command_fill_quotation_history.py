from apps.quotation.management.commands.fill_quotation_history import Command


class TestCommandFillQuotationHistory:
    def test_command_handler(self, mocker):
        # arrange
        mock_collect_coin_quotation_history = mocker.patch("apps.quotation.management.commands.fill_quotation_history.collect_coin_quotation_history")
        
        # act
        Command().handle()

        # assert
        mock_collect_coin_quotation_history.delay.assert_called_with(days=30)