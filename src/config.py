import os


MAX_QUESTIONS_PER_EPISODE = 12
ANSWER_TIMEOUT = 10  # seconds
MIN_TIME_BETWEEN_QUESTIONS = 60  # seconds

EPISODE_WORKER_MSG_DELAY = 60
# so that we can send notification to clients
SET_START_TIME_IN_FUTURE_SECONDS = 60

RESPONSE_RESOURCE_NAME = "response"
EPISODE_RESOURCE_NAME = "episode"
GAME_RESOURCE_NAME = "game"
PARTICIPANT_RESOURCE_NAME = "participant"
RESPONSE_STAT_RESOURCE_NAME = "responsestat"
QUESTION_RESOURCE_NAME = "question"
MAX_OPTIONS_IN_A_QUESTION = 3

DDB_TABLE_ENV_MAP = {
    RESPONSE_RESOURCE_NAME: "ResposeDBTableName",
    PARTICIPANT_RESOURCE_NAME: "ParticipantDBTableName",
    GAME_RESOURCE_NAME: "GameDBTableName",
    QUESTION_RESOURCE_NAME: "QuestionDBTableName",
    EPISODE_RESOURCE_NAME: "EpisodeDBTableName",
    RESPONSE_STAT_RESOURCE_NAME: "ResposeStatisticsDBTableName"
}

env_keys = os.environ.keys()

if "EpisodeWorkerSQSURL" in env_keys:
    EPISODE_WORKER_SQS_QUEUE_URL = os.environ["EpisodeWorkerSQSURL"]
else:
    EPISODE_WORKER_SQS_QUEUE_URL = "https://localhost:8443/sqs/EPISODE_WORKER_SQS_QUEUE"
