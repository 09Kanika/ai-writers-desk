import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## function to get respnse from LLAMA 2

def getLLAMAresponse(content_type,input_text_field,num_words,incluence_style):

    llm=CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    #template prompt
    template="""
        Write a {content_type} for {incluence_style} job profile, 
        for a topic {input_text_field} within {num_words} words.
        provide title then in next line give introduction and them in next line provide the body.
        """

    prompt=PromptTemplate(input_variables=["content_type","incluence_style","input_text_field","num_words"],
                          template=template)
    
    #generate response from llama 2

    if (content_type=='Blog'):
        template="""
                 i want you to generate a {content_type} for {incluence_style} job profile in a very precise manner, 
                 it should provide a proper title and introduction, also it should follow the {content_type} format.  """
    elif (content_type=='Article'):
        template="""
                 i want you to generate a {content_type} for {incluence_style} job profile in a very precise manner, 
                 it should provide a proper title and introduction, also it should follow the {content_type} format.  """
    elif (content_type=='Essay'):
        template="""
                 i want you to generate a {content_type} for {incluence_style} job profile in a very precise manner, 
                 it should provide a proper title and introduction, also it should follow the {content_type} format.  """
    

    response=llm(prompt.format(content_type=content_type,incluence_style=incluence_style,input_text_field=input_text_field,num_words=num_words))
    print(response)
    return response



st.set_page_config(page_title="AI Writer's Desk",
                   page_icon='🖥️',
                   layout='centered',
                   initial_sidebar_state='collapsed')
header_col1, header_col2, header_col3= st.columns([1,2,1])
with header_col2:
    st.header("AI Writer's Desk 🖥️")

st.markdown("<br>", unsafe_allow_html=True)
content_type=st.selectbox("What do you desire to generate?",('Blog','Article','Essay'),index=0)

st.markdown("<br>", unsafe_allow_html=True)
input_text_field=st.text_input("Share the exciting topic for your content: ")


## create 2 more columns for additional 2 fields

col1,col2=st.columns([5,5])
with col1:
    num_words=st.text_input("Number of words")
with col2:
    incluence_style=st.selectbox("Writing the blog to influence ",('','Architects','Journalists','Doctors', 'Scientists',
                                                                   'Machine Learning Engineers','Engineers','Fashion Designers',
                                                                   'Teachers','Students','Parents','Common People'),index=0)



st.write("Click here to generate your Blog")
submit = st.button("Generate")

if submit:
    st.write(getLLAMAresponse(content_type,input_text_field,num_words,incluence_style))

