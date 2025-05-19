import streamlit as st

st.set_page_config(page_title="BMI Calculator")

st.title("⚖️ Калькулятор индекса массы тела")

st.markdown("Введите ваши параметры:")

# Ввод пользователя
height = st.number_input("Рост (в см):", min_value=50, max_value=250, value=170)
weight = st.number_input("Вес (в кг):", min_value=10, max_value=300, value=70)

# Расчет ИМТ
if height > 0 and weight > 0:
    bmi = weight / ((height / 100) ** 2)
    st.markdown(f"### Ваш ИМТ: {bmi:.2f}")

    # Интерпретация
    if bmi < 18.5:
        st.warning("Недостаточный вес")
    elif 18.5 <= bmi < 24.9:
        st.success("Нормальный вес")
    elif 25 <= bmi < 29.9:
        st.warning("Избыточный вес")
    else:
        st.error("Ожирение")