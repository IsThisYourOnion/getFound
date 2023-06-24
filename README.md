# GetFound: Master Keyword Resume Generator

## Project Overview

GetFound, currently in its first completed version (v1), is an ongoing project revolving around the creation of a **Master Keyword Resume**. It should be noted that GetFound is *not a job-ready resume builder*, but it specifically capitalizes on LinkedIn's resume sharing [feature](https://www.linkedin.com/help/linkedin/answer/a1327213/share-and-manage-your-resumes-with-recruiters?lang=en)

The objective of GetFound is to devise a resume abundant in industry and role-specific keywords. This strategy leverages the algorithmic systems used by many job posting platforms that analyze stored resumes for relevant keywords to locate suitable candidates.

By utilizing **Large Language Models (LLMs)** for key phrase extraction and text similarity, GetFound ensures that the output template's resultant keywords align closely with your particular search queries. The outcome is an enhanced job search process and increased visibility of your resume to recruiters and employers, thanks to the incorporation of the most relevant and in-demand industry keywords.

## Workflow

GetFound's operation is split into two primary phases:

1. **Data Collection**: By leveraging powerful Python web scraping libraries, the project automates the collection of relevant job descriptions from LinkedIn. It searches for job postings using specific keywords, fetches the descriptions, and stores them for further processing.

2. **Keyword Extraction and Resume Compilation**: In this subsequent phase, GetFound processes the gathered job descriptions using LLMs to identify common and critical keywords. These keywords are then integrated into the master keyword resume, ensuring it is highly relevant and attractive to job posting services.

While GetFound continues to evolve, its current version (v1) already includes resume building features. However, these are not intended for immediate job applications. Instead, it is specifically designed to enhance the resume sharing feature of LinkedIn. Here, your profile gains greater visibility in search results when recruiters seek skills and experiences matching the data in the resumes you've saved over the past two years.

## Project Impact

By automating the often laborious process of customizing a resume for each job application, GetFound can significantly boost a candidate's visibility across job search platforms and make job hunting more efficient and effective.

## Future Developments

Stay tuned for future updates and improvements to the GetFound project. This tool is committed to making your job search more effective, especially in the context of LinkedIn's resume sharing feature.
