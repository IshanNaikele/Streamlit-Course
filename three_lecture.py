import streamlit as st

st.title("Learning Streamlit")

col1,col2=st.columns(2)

with col1:
    st.header("Cricket")
    st.image("https://tse3.mm.bing.net/th/id/OIP.0teqvh4Db5cg-wO072dpbgHaFk?pid=Api&P=0&h=180", use_container_width=True)
    vote1=st.button("Vote for Cricket")

with col2:
    st.header("Chess")
    st.image("https://tse1.mm.bing.net/th/id/OIP.PbRqdryMvSX9A-LbQoCyLgHaE8?pid=Api&P=0&h=180", use_container_width=True)
    vote2=st.button("Vote for Chess")


if vote1:
    st.success("Thanks for Voting for Cricket")
elif vote2:
    st.success("Thanks for Voting for Chess") 

name=st.sidebar.text_input("Enter Your Name")
bevarage=st.sidebar.selectbox(f"Choose your favourite bevarage.",['--Select--','Chai','Coffeee'])
if vote1 :
    st.write(f"Hello {name},Enjoy the {bevarage} while watching your favourite sports Cricket.")
elif vote2 :
    st.write(f"Hello {name},Enjoy the {bevarage} while watching your favourite sports Chess .")

with st.expander("How to make a Chai ?"):
    st.write("""
            1.Turn on the Gas.\n
            2.Boil the Water.\n
            3.Pour Milk and Tea patti.\n
            4.Add Sugar\n
            5.Boil it for 5 minute .\n\n\n\n\n\n
             
            ------- Your Chai is Ready -------
             """)
    
st.markdown("# Welcome to Streamlit Course")