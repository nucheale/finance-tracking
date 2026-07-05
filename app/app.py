import streamlit as st
from database import create_tables


class StreamliApp:
    PAGE_TITLE = "Учет расходов"
    PAGE_ICON = ":material/currency_ruble:"
    PAGES = {
        "Главное": [
            st.Page("./app/pages/stats.py", title="Ваши расходы"),
            st.Page("./app/pages/upload.py", title="Загрузка выписок"),
        ]
    }

    def __init__(self) -> None:
        self._init_database()
        self._set_navigation(self.PAGES)
        self._set_page_config()

    @staticmethod
    def _init_database() -> None:
        create_tables()

    def _set_navigation(self, pages: dict) -> None:
        st.navigation(pages).run()

    def _set_page_config(self) -> None:
        st.set_page_config(
            page_title=self.PAGE_TITLE,
            layout="wide",
            page_icon=self.PAGE_ICON,
            initial_sidebar_state="expanded",
        )
