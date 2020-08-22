import datetime
import logging
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('関数の呼び出しがスケジュールよりも遅れています')

    logging.info('Pythonのタイマートリガー関数が%sに実行されました', utc_timestamp)
