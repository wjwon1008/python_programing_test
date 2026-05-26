import streamlit as st

st.title('웹웹')

'GENESIS MAGMA RACING'

'# :blue[시각화 라이브러리]'
'#### :orange[Matplotlib: sy.pyplot()]'

import matplotlib.pyplot as plt

x= np.linspace(0, 10, 100)
y= np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y)
st.pyplot(fig) # 차트 출력
