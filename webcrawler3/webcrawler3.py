# https://selenium-python.readthedocs.io/getting-started.html
# https://beautiful-soup-4.readthedocs.io/en/latest/
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from random import randint
import csv

from webdriver_manager.chrome import ChromeDriverManager

#Chromedriver can be downloaded here :https://chromedriver.chromium.org/
# Or the chrome driver can be downloaded anew everytime the program starts.(Takes about 3 seconds). This also avoids the problem where if your chrome browser and the chrome browser are on different updates, an error would occur.
#driver = webdriver.Chrome(ChromeDriverManager().install())
#maximize window so that when a job is clicked on, it is shown on the left side of the page. Otherwise there is an error.
#driver.maximize_window()
# On the linkedin job search function. Apply the filters that you want and then copy that url and paste it here underneath 
#url = 'https://www.linkedin.com/jobs/search/?currentJobId=3256415012&f_C=3533853&geoId=92000000'
# Change this as well when you run the code, it changes the name of the csv file
company_name_csv = "1"
urls = ["https://www.linkedin.com/jobs/search/?currentJobId=3628521917&f_C=2502171&geoId=92000000&originToLandingJobPostings=3628521917%2C3645641788%2C3646640543%2C3641905453%2C3644677363%2C3636443727%2C3645649115%2C3642876315%2C3632128258", "https://www.linkedin.com/jobs/search/?currentJobId=3617387425&f_C=3334773&geoId=92000000&originToLandingJobPostings=3617387425%2C3503852949%2C3641003807%2C3578935947%2C3651425521%2C3641602681%2C3609339141%2C3651420838%2C3615806525", "https://www.linkedin.com/jobs/search/?currentJobId=3146895406&f_C=71851558&geoId=92000000&originToLandingJobPostings=3146895406%2C3581729745%2C3647085299%2C3634797119%2C3149976919%2C3625949725%2C3603163618%2C3589228345%2C3538332436"]


new_unicorns_list = [6, 8, 9, 11, 14, 20, 21, 24, 26, 27, 30, 32, 36, 39, 40, 41, 45, 49, 51, 56, 57, 58, 59, 60, 64, 66, 67, 68, 69, 70, 73, 74, 75, 79, 80, 82, 85, 86, 88, 89, 91, 95, 97, 98, 99, 102, 107, 108, 111, 114, 115, 121, 127, 130, 131, 137, 139, 140, 142, 145, 149, 150, 152, 153, 154, 155, 156, 160, 162, 163, 167, 169, 172, 175, 176, 177, 178, 179, 184, 185, 186, 189, 191, 196, 197, 199, 202, 203, 204, 208, 211, 212, 214, 215, 217, 218, 220, 221, 223, 224, 225, 228, 229, 231, 233, 234, 237, 239, 240, 241, 244, 245, 247, 248, 249, 250, 251, 254, 256, 261, 262, 263, 264, 267, 269, 270, 272, 273, 274, 275, 276, 278, 282, 283, 290, 292, 293, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 307, 309, 312, 314, 316, 318, 321, 323, 325, 328, 329, 330, 331, 333, 335, 336, 339, 340, 342, 343, 344, 345, 346, 347, 349, 351, 353, 354, 355, 357, 359, 360, 361, 362, 364, 366, 367, 370, 371, 373, 374, 375, 381, 382, 383, 385, 386, 387, 392, 398, 400, 401, 402, 405, 406, 407, 408, 409, 414, 416, 417, 421, 423, 427, 428, 429, 430, 433, 434, 436, 442, 444, 445, 446, 447, 449, 453, 456, 458, 462, 464, 465, 466, 467, 471, 473, 477, 478, 479, 481, 487, 491, 493, 497, 498, 501, 502, 503, 505, 507, 509, 510, 511, 514, 516, 517, 518, 519, 522, 524, 525, 526, 528, 530, 532, 535, 538, 539, 540, 541, 543, 545, 546, 548, 550, 551, 555, 556, 558, 559, 560, 562, 563, 564, 567, 568, 569, 575, 577, 580, 581, 582, 583, 585, 586, 587, 591, 592, 593, 596, 598, 600, 601, 602, 610, 614, 615, 619, 620, 621, 626, 635, 636, 637, 638, 639, 640, 641, 643, 644, 645, 647, 648, 649, 652, 654, 656, 657, 658, 660, 663, 665, 668, 670, 672, 673, 674, 676, 680, 684, 690, 693, 694, 696, 697, 698, 700, 702, 703, 705, 707, 709, 712, 713, 717, 719, 723, 725, 726, 728, 729, 730, 735, 740, 741, 743, 750, 751, 752, 753, 754, 755, 761, 762, 763, 765, 766, 773, 775, 776, 777, 779, 783, 786, 789, 791, 792, 795, 797, 802, 803, 804, 807, 808, 814, 815, 816, 821, 823, 824, 826, 827, 828, 829, 831, 832, 833, 835, 836, 838, 839, 844, 845, 847, 848, 850, 855, 858, 861, 862, 863, 865, 868, 869, 870, 871, 872, 874, 876, 877, 878, 879, 882, 884, 885, 887, 888, 889, 891, 894, 895, 896, 898, 901, 902, 903, 904, 905, 907, 908, 909, 910, 913, 914, 919, 924, 929, 932, 938, 940, 942, 948, 950, 952, 954, 955, 956, 957, 961, 963, 973, 978, 981, 987, 991, 997, 1000, 1002, 1004, 1005, 1012, 1013, 1014, 1018, 1019, 1021, 1022, 1024, 1026, 1027, 1028, 1029, 1031, 1032, 1034, 1035, 1036, 1039, 1040, 1041, 1042, 1043, 1048, 1049, 1052, 1055, 1056, 1057, 1063, 1064, 1065, 1066, 1068, 1069, 1070, 1071, 1074, 1076, 1077, 1079, 1081, 1083, 1084, 1085, 1086, 1090, 1091, 1092, 1093, 1094, 1095, 1097, 1104, 1109, 1112, 1113, 1114, 1117, 1118, 1119, 1122, 1123, 1124, 1127, 1128, 1131, 1132, 1134, 1137, 1138, 1139, 1141, 1142, 1144, 1146, 1148, 1149, 1150, 1151, 1154, 1156, 1158, 1160, 1162, 1163, 1164, 1165, 1166, 1172, 1173, 1176, 1178, 1180, 1181, 1182, 1184, 1186, 1187, 1188, 1189, 1190, 1195, 1197, 1203, 1204, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1214, 1215]
i_name = 587
for url in urls:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    i_name = i_name + 1

    driver.get(url)
    time.sleep(3)
    #If this returns an error, restart the browser/program. Maybe put it in a Try/catch block to automatically restart it.
    no_of_jobs = driver.find_element_by_css_selector('h1>span').get_attribute('innerText')
    print(no_of_jobs)
    # If the number is really large, it is often represented with a plus at the end like 100000+ so I remove this '+' symbol
    for char in '+,':
        no_of_jobs = no_of_jobs.replace(char, '')

    no_of_jobs = int(no_of_jobs)
    if no_of_jobs > 1000:
        no_of_jobs = 1200
    i = 2
    #"show more" can be clicked a maximum of 34 times before it does not show more.
    #shows only maximum 1000 jobs per filter. So one would need to use multiple filters to get all available jobs.
    #cookies = driver.find_element_by_css_selector(".artdeco-global-alert-action__wrapper")
    #cookies.find_elements_by_css_selector('.artdeco-global-alert-action.artdeco-button.artdeco-button--inverse.artdeco-button--2.artdeco-button--primary')[1].click()
    while i <= int(no_of_jobs/25) + 1:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        i = i + 1
        set1 = driver.find_elements_by_css_selector('button.infinite-scroller__show-more-button.infinite-scroller__show-more-button--visible')
        for a in set1:
            a.click()

        time.sleep(5)
    #WScroll back to the top. Otherwise the click does not work.
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

    job_lists = driver.find_element_by_class_name('jobs-search__results-list')
    jobs = job_lists.find_elements_by_tag_name('li')

    #print(len(jobs))

    #the data from job description ("jd") is so far the only reliable outcome.
    job_title = []
    company_name = []
    location = []
    date = []
    job_link = []

    jd = []
    seniority = []
    emp_type = []
    job_func = []
    industries = []

    for job in jobs:
        jd0 = []
        job_func0=[]
        industries0=[]
 
        job_title0 = job.find_element_by_css_selector('h3').get_attribute('innerText')
        job_title.append(job_title0)
 
        company_name0 = job.find_element_by_css_selector('h4').get_attribute('innerText')
        #company_name.append(company_name0)
        company_name.append(str(new_unicorns_list[i_name]))
 
        location0 = job.find_element_by_css_selector('[class="job-search-card__location"]').get_attribute('innerText')
        location.append(location0)
 
        date0 = job.find_element_by_css_selector('div>div>time').get_attribute('datetime')
        date.append(date0)
 
        job_link0 = job.find_element_by_css_selector('a').get_attribute('href')
        print(job_link0)
        job_link.append(job_link0)
        job.find_element_by_css_selector('a').click()
        time.sleep(randint(5,8))
        #/html/body/div[1]/div/section/div[2]/div/section[1]/div/div/section/div/text()[1]
    
        jd_path = '/html/body/div[3]/div/section/div[2]/div/section[1]/div/div/section/div'
        #jd_elements = job.find_element(By.CSS_SELECTOR, '.show-more-less-html__markup.show-more-less-html__markup--clamp-after-5')
        if job.find_elements_by_xpath(jd_path):
            jd_elements = job.find_elements_by_xpath(jd_path)
            for element in jd_elements:
                jd0.append(element.get_attribute('innerText'))
                jd_final = ', '.join(jd0)
                jd.append(jd_final + ' ')

        else:
            jd.append('NULL')
        #Path to seniority
        seniority_path = '/html/body/div[3]/div/section/div[2]/div/section[1]/div/ul/li[1]/span'

        if job.find_element_by_xpath(seniority_path):
            seniority0 = job.find_element_by_xpath(seniority_path).get_attribute('innerText')
            seniority.append(seniority0)
        else:
            seniority.append('NULL')

        #Path to employment type
        emp_type_path = '/html/body/div[3]/div/section/div[2]/div/section[1]/div/ul/li[2]/span'
        emp_type_path0 = '/html/body/div[3]/div/section/div[2]/div/section/div/ul/li/span'

        try:
            if job.find_element_by_xpath(emp_type_path):
                emp_type0 = job.find_element_by_xpath(emp_type_path).get_attribute('innerText')
                emp_type.append(emp_type0)
            else:
                emp_type.append('NULL')
        except:
            if job.find_element_by_xpath(emp_type_path0):
                emp_type0 = job.find_element_by_xpath(emp_type_path0).get_attribute('innerText')
                emp_type.append(emp_type0)
            else:
                emp_type.append('NULL')

    
        #Path to Job Function
        job_func_path = '/html/body/div[3]/div/section/div[2]/div/section[1]/div/ul/li[3]/span'

        if job.find_elements_by_xpath(job_func_path):
            job_func_elements = job.find_elements_by_xpath(job_func_path)
            for element in job_func_elements:
                job_func0.append(element.get_attribute('innerText'))
                job_func_final = ', '.join(job_func0)
                job_func.append(job_func_final)
        else:
            job_func.append('NULL')

        #Path to Industries
        industries_path = '/html/body/div[3]/div/section/div[2]/div/section[1]/div/ul/li[4]/span'

        if job.find_elements_by_xpath(industries_path):
            industries_elements = job.find_elements_by_xpath(industries_path)
            for element in industries_elements:
                industries0.append(element.get_attribute('innerText'))
                industries_final = ', '.join(industries0)
                industries.append(industries_final)
        else:
            industries.append('NULL')


    #headings for the csv file:
    headings = ["URL", "Title", "Company", "Location", "Date", "Description", "Seniority", "Employment Type", "Function", "Industries" ]
    #open csv file

    save_cvs_row = [job_link, job_title, new_unicorns_list[i_name], location, date, jd, seniority, emp_type, job_func, industries]

    #  + str(i_name) +
    with open('C:/Users/Admin/source/repos/WI23/New Unicorn Jobs' + str(new_unicorns_list[i_name]) + '.csv', 'w', encoding='utf-8', newline = '') as fi:
        #create csv writer
        writer = csv.writer(fi)
        writer.writerow(headings)
        for a, b, c, d, e, f, g, h, i, j in zip(job_link, job_title, company_name, location, date, jd, seniority, emp_type, job_func, industries):
            row = [a, b, c, d, e, f, g, h, i, j]
            writer.writerow(row)
        fi.close()

    driver.quit()

