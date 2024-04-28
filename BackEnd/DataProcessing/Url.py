NEWS_API_URL = "http://j10c107.p.ssafy.io:8080/api/v1/news"
KEYWORDS_API_URL = "http://j10c107.p.ssafy.io:8080/api/v1/keywords"
DUPLICATENEWS_PATH = "/usr/src/app/NewsCrawling/DuplicateNews"
DAYS_NEWS_PATH = "/usr/src/app/Hadoop/data/DaysNews"
TF_IDF_BASE_NAME = "TF-IDF.txt"
LOCAL_INPUT_PATH = f"/home/ubuntu/newsData/Input/{TF_IDF_BASE_NAME}"
LOCAL_OUTPUT_PATH = f"/home/ubuntu/newsData/Output/{TF_IDF_BASE_NAME}"
DOCKER_INPUT_PATH = f"/usr/src/app/Hadoop/data/Input/{TF_IDF_BASE_NAME}"
DOCKER_OUTPUT_PATH = f"/usr/src/app/Hadoop/data/Output/{TF_IDF_BASE_NAME}"
EC2_IP = "3.36.72.23"
USER_NAME = "ubuntu"
KEY_FILE_URL = "/usr/src/app/Hadoop/data/J10C107T.pem"