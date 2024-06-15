import streamlit as st 

st.title('HELLO GEEKS')

st.header('Header - > GeeksForGeeks')

st.subheader('Subheader -> GeekforGeeks')

st.markdown('# Hi')

st.markdown('## Hi')

st.markdown('### Hi')

st.markdown('#### Hi')

st.markdown('##### Hi')

st.markdown('Hi')

st.success('SUCCESSFULLY DONE')

st.info('HERE COMES THE INFORMATION')

st.warning('WARNING MESSAGE')

st.error('ERROR')

st.exception(ZeroDivisionError('DIVISION NOT POSSIBLE '))

st.help(ZeroDivisionError)

st.write('sample ')

st.write(range(1,10))

st.write(5*100)

st.code('x=10\n' 
        'for i in range(x):\n'
        '\tprint(i)'
        )

st.checkbox('Male')
if(st.checkbox('Adult')):
    st.write('You are an adult')

radioButton = st.radio('Select from below: ' , ('Male' , 'Female' , 'Other'))

if(radioButton == 'Male'):
    st.write('You are a male')

if(radioButton == 'Female'):
    st.write('You are a Female')

if(radioButton == 'Other'):
    st.write('You are an other gender')
    

st.subheader('Select Box')

selectBox = st.selectbox('Data Science :' , ['Data Analsis' , 'Web Scrapping' , 'Machine Learning' , 'Deep Learning' ,
                                 'Natural Language Processing' , 'computer Vision' , 'Image Processing'])

st.write("You've selected :" , selectBox)

st.subheader('Multiselect Box')

multiselected = st.multiselect('Data Science :' , ['Data Analsis' , 'Web Scrapping' , 'Machine Learning' , 'Deep Learning' ,
                                 'Natural Language Processing' , 'computer Vision' , 'Image Processing'])

st.write("You have selected: ", len(multiselected) , multiselected)

st.subheader('Button')

if(st.button('click here')):
    st.write('You have come a long way')

st.subheader('Slider')
vol = st.slider('Select the volume' , 0 , 100 , step = 1)
st.write('Volume is :' , vol)

st.subheader('Text Input')
name = st.text_input('Name: ' )
password = st.text_input('Password : ' , type= 'password')
st.write('Hi. ', name)

st.subheader('Text Area')
textarea = st.text_area('Describe your feelings over here' , max_chars=100)
st.write(textarea)

st.subheader('Input Number')
st.number_input('Select your age' , 18 , 110)

st.subheader('Input Date')
st.date_input('Date')

st.subheader('Input Time')
st.time_input('Time')

