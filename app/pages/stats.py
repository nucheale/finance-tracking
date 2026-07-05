import streamlit as st
import locale
from app.pages.base import BasePage


locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")


class StatsPage(BasePage):
    def set_header(self, header):
        st.header(header)

    @staticmethod
    def format_price(price: float | int) -> str:
        return locale.format_string("%.2f", price, grouping=True)

    def set_metric(self) -> None:
        metric_cols = st.columns([1, 1, 1, 4])
        with metric_cols[0]:
            v1 = 53425.34
            st.metric(
                label="Расходы за месяц",
                value=self.format_price(v1),
                border=True,
                delta_color="blue",
                delta="-93 321,00",
                width="stretch",
            )
        with metric_cols[1]:
            v2 = 423
            st.metric(
                label="Средняя сумма покупки",
                value=self.format_price(v2),
                border=True,
                delta_color="grey",
                delta="23,00",
                width="stretch",
            )
        with metric_cols[2]:
            v3 = 14333
            st.metric(
                label="Самая крупная покупка",
                value=self.format_price(v3),
                border=True,
                delta_color="violet",
                delta="3 321,00",
                width="stretch",
            )

    def render(self):
        self.set_header("Расходы")
        self.set_metric()


StatsPage().render()
