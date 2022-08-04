## Job scraping bot on Linkedin Website

A simple bot script using selenium to scrape job details from Linkedin job posting domain.

#### Explanation

In this project, I have used Selenium library to automate the scraping process. Before scraping job details, Selenium automated steps below:

>Automated Steps
1. Open Chrome browser and navigate to Linkedin login page
2. Fill-in E-Mail Address and Password areas and click Login 
3. Navigate to job search website
4. Search for job positions *(Data Analyst)* in Hanoi *(Could be anywhere from the world)*
5. Scroll down each job card to collect information.
6. Go to the next page when all card have been selected and scraped.

>Items Scraped:
1. Job Title
2. Company Name
3. Company Location
4. Working Method (Hybrid, Remote, On-Site)
5. Working duration (Full-time, Part-time)
6. Position offered
7. Salary (if any)
8. Company size
9.  Company sector
10. Post date
11. Number of applicants
12. Job Description

#### To use the script

Install selenium package 

```python
pip install selenium
```

#### Sample result

![Capture](https://user-images.githubusercontent.com/97393390/182823037-064994f6-33e8-4ad3-81c3-3a133f54dd44.PNG)
