"""
@brief  This script runs the FlaskWeb application using a development server.
"""
import time
import threading
from os import environ
from FlaskWeb import app, socketio


# Define a function for the thread
def print_time(thread_name, delay):
    """
    @brief  function for counting time for 5 count
    :param thread_name: String to store the name of the Thread
    :param delay: Delay between counts - Sleep length
    :return: - Nothing -
    """
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))


if __name__ == '__main__':
    # HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    # Run the Flask Application
    # app.run('0.0.0.0', PORT)
    try:
        # Test threading for a future addition
        #t = threading.Thread(target=print_time, args=('Thread 1', 2, ))
        #t.start()
        pass

    except:
        print("Error: Unable to start thread")


    socketio.run(app, host='0.0.0.0', port=PORT)
