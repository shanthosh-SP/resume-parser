import streamlit as st
import os
import pandas as pd
from resume_parser import resumeparse
from pyresparser import ResumeParser
import nltk
#nltk.download('stopwords')
def file_selector(folder_path='Resumes'):
	filename=os.listdir(folder_path)
	selected_filename=st.selectbox('select a file',filename)
	return os.path.join(folder_path,selected_filename)
if st.button("Process"):
	filename=file_selector()
	st.write("You selected `%s` " %filename)


	Skills_extraction=ResumeParser(filename).get_extracted_data()
	extract_for_YoE=resumeparse.read_file(filename)
# df=pd.DataFrame()
# df=df.append(data,ignore_index=True)
# cols=list(df)
# cols.insert(0,cols.pop(cols.index('name')))
# df=df.reindex(columns=cols)
# st.write(df[cols])

# st.subheader("Skills from resume")
# st.table(df['skills'])
# st.subheader("Experience from resume")
# st.table(df['experience'])
#st.write("Name----",extract_for_YoE['name'])
#st.write("Skills----",Skills_extraction['skills'])
#st.write("Years of Experience-----",extract_for_YoE['total_exp'])

	Skills_extracted=Skills_extraction['skills']

	skills_reqd_DS=['machine learning','data mining','predictive modeling', 'statistical analysis', 'data visualization', 'natural language processing', 'big data', 'data warehousing', 'sql', 'python/r programming', 'deep learning', 'artificial intelligence', 'data analytics', 'a/b testing', 'feature engineering', 'etl processes', 'time series analysis', 'regression analysis', 'cluster analysis', 'decision trees']
	skills_reqd_HR=['job postings', 'applicant tracking systems (ats)', 'candidate sourcing', 'interviewing skills', 'hiring process', 'job descriptions', 'talent acquisition', 'diversity and inclusion', 'background checks', 'onboarding']
	skills_reqd_sales=['objection handling', 'social selling', 'lead generation', 'business development', 'account management', 'client relationship management', 'sales forecasting', 'sales strategy', 'sales negotiations', 'pipeline management', 'territory management', 'lead generation', 'customer acquisition', 'sales performance', 'sales reporting']


	Skills_extracted=[x.lower() for x in Skills_extracted]
	Skills_extracted=[num.strip(' ') for num in Skills_extracted]
	Skills_extracted=[num.strip(')') for num in Skills_extracted]
	Skills_extracted=[num.strip('(') for num in Skills_extracted]

#st.write("Skills",Skills_extracted)
	res={'skills_reqd_DataScientist':[],'skills_reqd_HR':[],'skills_reqd_sales':[]}
	for i in Skills_extracted:
		if i in skills_reqd_DS:
			res['skills_reqd_DataScientist'].append(str(i))
		if i in skills_reqd_HR:
			res['skills_reqd_HR'].append(str(i))
		if i in skills_reqd_sales:
			res['skills_reqd_sales'].append(str(i))
   



	HR=0
	DS=0
	sales=0
	x=1
	c="He is Specialised in"
	b=""
	for i,j in res.items():

		if x==1:
			DS=len(j)
		if x==2:
			HR=len(j)
		if x==3:
			sales=len(j)
		x+=1
	if (HR>DS and HR>sales):
		b="HR"
		print('He is applicable for HR role')
	if (DS>HR and DS>sales):
		b="DataScientist"
		print('He is applicable for DataScientist role')
	if (sales>HR and sales>DS):
		b="Sales"
		print('He is applicable for Sales role')

	print(c+' '+b)

import pandas as pd

	sal_data=pd.read_csv(r"Sal_data.csv")
	sal_data.info()

	sal_data=pd.DataFrame(sal_data)
	a=extract_for_YoE['total_exp']

	st.write(a,b)

	def final(a,b):
		if a<=2 and b=="DataScientist":
			color_and_shape = sal_data.loc[(sal_data['Job Role'] == "DataScientist") & (sal_data['YoE'] == "0-2")]
			st.write(color_and_shape)

		if   2 < a <=4 and b=="DataScientist":
			color_and_shape = sal_data.loc[(sal_data['Job Role'] == "DataScientist") & (sal_data['YoE'] == "2-4")]
			st.write(color_and_shape)

		if 4< a <=10 and b=="DataScientist":
			color_and_shape = sal_data.loc[(sal_data['Job Role'] == "DataScientist") & (sal_data['YoE'] == "5-10")]
			st.write(color_and_shape)

		if a>=11 and b=="DataScientist":
			color_and_shape = sal_data.loc[(sal_data['Job Role'] == "DataScientist") & (sal_data['YoE'] == "10+")]
			st.write(color_and_shape)
		if a<=2 and b=="HR":
			color_and_shape = sal_data.loc[(sal_data['Job Role'] == "HR") & (sal_data['YoE'] == "0-2")]
			st.write(color_and_shape)

		if 2 < a <=4 and b=="HR":
			color_and_shape = sal_data.loc[(sal_data['Job Role'] == "HR") & (sal_data['YoE'] == "3-4")]
			st.write(color_and_shape)

		if 4 < a <=10 and b=="HR":
			color_and_shape = sal_data.loc[(sal_data['Job Role'] == "HR") & (sal_data['YoE'] == "5-10")]
			st.write(color_and_shape)
		if a>=11 and b=="HR":
			color_and_shape = sal_data.loc[(sal_data['Job Role'] == "HR") & (sal_data['YoE'] == "10+")]
			st.write(color_and_shape)

	# else:
	# 	st.write("bye")
	final(extract_for_YoE['total_exp'],b)
        
