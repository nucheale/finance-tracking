import streamlit as st
from app.pages.base import BasePage
from logic.parsers import read_xlsx



class UploadPage(BasePage):
    def set_header(self, header):
        st.header(header)

    def render(self):
        self.set_header("Загрузка")
        file = st.file_uploader("Загрузка выписки", width=400)
        if file:
            st.dataframe(read_xlsx(file))

UploadPage().render()
