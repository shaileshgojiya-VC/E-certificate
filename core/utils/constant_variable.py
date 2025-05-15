## Constant String ##

GENDER_MALE = "Male"
GENDER_FEMALE = "Female"

## Constants Status ##
STATUS_SUCCESS = "success"
STATUS_FAIL = "fail"
STATUS_ERROR = "error"
STATUS_NULL = None
STATUS_TRUE = True
STATUS_FALSE = False
API_V1 = "/v1"
API_V2 = "/v2"
API_v1 ="/api/v1"

## Constant Number ##
STATUS_ZERO = 0
STATUS_ONE = 1
STATUS_TWO = 2
STATUS_THREE = 3
STATUS_FOUR = 4
STATUS_FIVE = 5
STATUS_SIX = 6
STATUS_SEVEN = 7
STATUS_EIGHT = 8
STATUS_NINE = 9
STATUS_TEN = 10

## Constant Date ##
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

## Constant API ##
CONTENT_TYPE_JSON = "application/json"
CONTENT_TYPE_XML = "application/xml"
AUTH_HEADER = "Authorization"
X_API_KEY_HEADER = "X-API-KEY"

## Database Constants ##
DB_TYPE_POSTGRESQL = "postgresql"
DB_TYPE_MYSQL = "mysql"
DB_TYPE_SQLITE = "sqlite"
DB_TYPE_ORACLE = "oracle"

## Constant User Roles ##
ROLE_ADMIN = "admin"
ROLE_USER = "user"
ROLE_GUEST = "guest"

## Constant Settings ##
MAX_RETRIES = 3
TIMEOUT_LIMIT = 30  # in seconds

## Pagination Constants ##
DEFAULT_PAGE_SIZE = 20
DEFAULT_PAGE_NUMBER = 1
MAX_PAGE_SIZE = 100

## Time and Date Constants ##
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_WEEK = 7
DAYS_IN_YEAR = 365

## Regular Expressions Patterns ##
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
PHONE_NUMBER_REGEX = r"^\+?[1-9]\d{1,14}$"

## File Types ##
FILE_TYPE_TEXT = "text/plain"
FILE_TYPE_JSON = "application/json"
FILE_TYPE_CSV = "text/csv"
FILE_TYPE_PDF = "application/pdf"
FILE_TYPE_IMAGE_JPEG = "image/jpeg"
FILE_TYPE_IMAGE_PNG = "image/png"
FILE_TYPE_EXCEL = "application/vnd.ms-excel"
FILE_TYPE_MP4 = "video/mp4"
FILE_TYPE_MPEG = "audio/mpeg"

## Miscellaneous ##
MAX_FILE_SIZE_MB = 10
DEFAULT_LANGUAGE = "en"
TIMEZONE_UTC = "UTC"
TIMEZONE_EST = "US/Eastern"


# Status codes
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
HTTP_500_INTERNAL_SERVER_ERROR = 500

# Default roles
ADMIN_ROLE = "admin"
USER_ROLE = "user"
GUEST_ROLE = "guest"

# Default permissions
CREATE_PERMISSION = "create"
READ_PERMISSION = "read"
UPDATE_PERMISSION = "update"
DELETE_PERMISSION = "delete"

# Resource types
USER_RESOURCE = "user"
PROFILE_RESOURCE = "profile"
ROLE_RESOURCE = "role"
PERMISSION_RESOURCE = "permission"

# Permission format: action_resource
# Examples:
CREATE_USER = f"{CREATE_PERMISSION}_{USER_RESOURCE}"
READ_USER = f"{READ_PERMISSION}_{USER_RESOURCE}"
UPDATE_USER = f"{UPDATE_PERMISSION}_{USER_RESOURCE}"
DELETE_USER = f"{DELETE_PERMISSION}_{USER_RESOURCE}"

# Role permissions
ADMIN_PERMISSIONS = [
    CREATE_USER, READ_USER, UPDATE_USER, DELETE_USER,
    f"{CREATE_PERMISSION}_{ROLE_RESOURCE}", 
    f"{READ_PERMISSION}_{ROLE_RESOURCE}",
    f"{UPDATE_PERMISSION}_{ROLE_RESOURCE}", 
    f"{DELETE_PERMISSION}_{ROLE_RESOURCE}",
    f"{CREATE_PERMISSION}_{PERMISSION_RESOURCE}", 
    f"{READ_PERMISSION}_{PERMISSION_RESOURCE}",
    f"{UPDATE_PERMISSION}_{PERMISSION_RESOURCE}", 
    f"{DELETE_PERMISSION}_{PERMISSION_RESOURCE}"
]

USER_PERMISSIONS = [
    READ_USER,
    f"{READ_PERMISSION}_{PROFILE_RESOURCE}",
    f"{UPDATE_PERMISSION}_{PROFILE_RESOURCE}"
]

GUEST_PERMISSIONS = [
    f"{READ_PERMISSION}_{PROFILE_RESOURCE}"
]

PERMISSION_ASSIGNED_SUCCESS= "Permission Assigned Successfully!!"