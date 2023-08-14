from tradingview_ta import TA_Handler, Exchange, Interval
from func_LevelBreakdown import symbol_list
# import tradingview_ta



class Crypto:
    """Класс для Определения покупки/продажи данной криптовалюты"""
    def __init__(self, symbol_val):
        self.symbol_val = symbol_val
        self.crypto = TA_Handler(
                symbol=self.symbol_val,
                screener="Crypto",
                exchange="BINANCE",
                interval=Interval.INTERVAL_1_HOUR
            )

    def __str__(self):
        try:
            result = self.crypto.get_analysis().summary['RECOMMENDATION']
            match result:
                case 'BUY':
                    return f"Мы рекомендуем покупку {self.crypto.symbol}"
                case 'SELL':
                    return f"Мы рекомендуем продажу {self.crypto.symbol}"
                case _:
                    return (f"Мы рекомендуем воздержаться от покупки "
                            f"или продажи {self.crypto.symbol}")
        except:
            return f"Монеты {self.symbol_val} нет на фьючерсах Binance"

if __name__ == "__main__":
    for item in symbol_list:
        print(Crypto(item))
