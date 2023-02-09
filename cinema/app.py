import pickle
import streamlit as st
st.header('Cinema Sales Prediction')
st.image('cinema.jpg')
lr = pickle.load(open('ticket.sav','rb'))
pred=[]
pred_list=[]
price=st.number_input('Ticket price', min_value=500, max_value=1000000, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False)
pred.append(price)
occ=st.number_input('Occupied per', min_value=0, max_value=150, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False)
pred.append(occ)
show=st.number_input('Show Time', min_value=0, max_value=50, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False)
pred.append(show)
sold=st.number_input('Tickets sold', min_value=0, max_value=50, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False)
pred.append(sold)
pred_list=[]
pred_list.append(pred)
if st.button("Predict ticket sales"):
    num=lr.predict(pred_list)
    st.text(f'The predicted ticket sales is {num[0]}')
