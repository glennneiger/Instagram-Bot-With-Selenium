

class ApplicationInfo:

    ####################################################################################################################
    # BOT INFO
    ####################################################################################################################

    RUN_CONTINUOUSLY = True
    NUMBER_OF_LIKES_PER_HASH_TAG = 20
    REDO_WHOLE_HASH_TAG_LIST = 3
    MIN_SECONDS_PER_LIKE = 5
    MAX_SECONDS_PER_LIKE = 15

    PAGE_LOAD_TIMEOUT = 30
    IMPLICIT_WAIT = 20
    SLEEP_TIME = 5

    # SHOULD AN EXCEPTION BE THROWN OF A BUTTON NOT FOUND
    # COPY XPATH OF BUTTON AND PASTE IT TO THEIR REPRESENTED FIELD DOWN BELOW

    # PATHS, CLASSES, TEXT STRINGS
    URL = 'http://www.instagram.com'
    LOG_IN_TEXT = 'Log in'
    USERNAME_TEXT = 'username'
    PASSWORD_TEXT = 'password'
    LOG_IN_BUTTON_PATH = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button'
    SEARCH_BAR_PATH = "//input[@class='XTCLo x3qfX ']"
    FIRST_LINK_CLASS = 'yCE8d'
    FIRST_SEARCH_IMAGE_PATH = '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a'
    LIKE_BUTTON_XPATH = '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'
    NEXT_TEXT = 'Next'
    CLOSE_BUTTON_PATH = "/html/body/div[4]/div/div/div[3]/button[2]"
    PROFILE_TEXT = 'Profile'

    # KEYWORDS
    COMMA_KEYWORD = ','
    HASH_TAG_KEYWORD = '#'
    STAGE0_KEYWORD = 'Stage 0: Starting Application'
    STAGE1_KEYWORD = 'Stage 1: Signing Into Instagram'
    STAGE2_KEYWORD = 'Stage 2: Going To Instagram.com'
    STAGE3_KEYWORD = 'Stage 3: Searching Images With HashTag'
    STAGE4_KEYWORD = 'Stage 4: Liking Images With Current HashTag'
    STAGE5_KEYWORD = 'Stage 5: Application Finished'

    # EXTRAS
    IMAGES_LIKED = 'Images Liked: '
    CLICKED_ON_FIRST_IMAGE = 'Clicked on first image'
    PICTURE_ALREADY_LIKED_TIME_OUT = '--Picture Already Liked It Inside Time Out: '
    PICTURE_ALREADY_LIKED_NO_SUCH_ELEMENT = '--Picture Already Liked It Inside No Such Element:'
