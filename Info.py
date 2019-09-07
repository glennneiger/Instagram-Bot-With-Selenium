class applicationInfo:

    ####################################################################################################################
    # BOT INFO
    ####################################################################################################################

    RUN_CONTINUOUSLY = True
    NUMBER_OF_LIKES_PER_HASH_TAG = 20
    REDO_WHOLE_HASH_TAG_LIST = 3
    MIN_SECONDS_PER_LIKE = 5
    MAX_SECONDS_PER_LIKE = 20

    PAGE_LOAD_TIMEOUT = 30
    IMPLICIT_WAIT = 20
    SLEEP_TIME = 5

    # PATHS, CLASSES, TEXT STRINGS
    URL = "http://www.instagram.com"
    LOG_IN_TEXT = 'Log in'
    USERNAME_TEXT = 'username'
    PASSWORD_TEXT = 'password'
    LOG_IN_BUTTON_PATH = "//button[contains(text(),'Log in')]"
    SEARCH_BAR_PATH = "//input[@class='XTCLo x3qfX ']"
    FIRST_LINK_CLASS = 'yCE8d'
    FIRST_SEARCH_IMAGE_PATH = '//span[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]/div[1]/a'
    LIKE_BUTTON_XPATH = '/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button'
    NEXT_TEXT = 'Next'
    CLOSE_BUTTON_PATH = "//button[text()='Close']"
    PROFILE_TEXT = 'Profile'

    # DRIVER PATH
    WEB_DRIVER = '\home\pirate\Programming\Pycharm\chromedriver.exe'

    # KEYWORDS
    COMMA_KEYWORD = ','
    HASH_TAG_KEYWORD = '#'
    STAGE1_KEYWORD = 'Stage 1: Going To WebSite'
    STAGE2_KEYWORD = 'Stage 2: Signing Into Instagram'
    STAGE3_KEYWORD = 'Stage 3: Searching Images With HashTag'
    STAGE4_KEYWORD = 'Stage 4: Liking Images With Current HashTag'
    STAGE5_KEYWORD = 'Stage 5: Application Finished'

    # ERRORS
    TIMEOUT_EXCEPTION_INSIDE = '--Failed Timeout Exception Inside Time In: '
    NOSUCHELEMENT_EXCEPTION_INSIDE = '--Failed No Such Element Inside Time In: '
    TIMEOUT_EXCEPTION_OUTSIDE = '--Failed Outside Time Out: '
    NOSUCHELEMENT_EXCEPTION_OUTSIDE = '--Failed Outside No Such Element: '

    # EXTRAS
    IMAGES_LIKED = 'Images Liked: '
    CURRENT_TAG = '--Current Hash Tag: '
    CLICKED_ON_FIRST_IMAGE = 'Clicked on first image'
    PICTURE_ALREADY_LIKED_TIME_OUT = '--Picture Already Liked It Inside Time Out: '
    PICTURE_ALREADY_LIKED_NO_SUCH_ELEMENT = '--Picture Already Liked It Inside No Such Element:'
