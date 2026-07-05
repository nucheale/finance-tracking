from abc import ABC, abstractmethod
import streamlit as st


class BasePage(ABC):
    @abstractmethod
    def set_header(self, header):
        st.header(header)

    
