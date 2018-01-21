import asyncio
import sys


try:
    from aiohttp import web
except ImportError:
    sys.exit("Cannot import from aiohttp. Do `pip3 install --user aiohttp` to install")

import cozmo


app = web.Application()


async def cozmo_say(request):
    '''Define an HTTP POST handler for receiving requests from If This Then That.

    You may modify this method to change how Cozmo reacts to
    an in-game update from IFTTT.
    '''

    json_object = await request.json()

    # Extract the text for the in-game update.
    alert_body = json_object["content"]

    robot = request.app['robot']
    async def read_name():
        try:
            #async with robot.perform_off_charger():
                '''If necessary, Move Cozmo's Head and Lift to make it easy to see Cozmo's face.'''
                # await robot.get_in_position()

                # First, have Cozmo play an animation
                # await robot.play_anim_trigger(cozmo.anim.Triggers.ReactToPokeStartled).wait_for_completed()

                # Next, have Cozmo speak the text from the in-game update.
                await robot.say_text(alert_body).wait_for_completed()

                # Last, have Cozmo display a sports image on his face.
                # robot.display_image_file_on_face("../face_images/ifttt_sports.png")
                # 或者变为图片展示中文 pil
                # 展示英文

        except cozmo.RobotBusy:
            cozmo.logger.warning("Robot was busy so didn't read update: '" + alert_body +"'")

    # Perform Cozmo's task in the background so the HTTP server responds immediately.
    asyncio.ensure_future(read_name())

    return web.Response(text="OK")

# Attach the function as an HTTP handler.
app.router.add_post('/cozmo_say', cozmo_say)


if __name__ == '__main__':

    cozmo.setup_basic_logging()
    cozmo.robot.Robot.drive_off_charger_on_connect = False


    try:
        app_loop = asyncio.get_event_loop()  
        sdk_conn = cozmo.connect_on_loop(app_loop)

        # Wait for the robot to become available and add it to the app object.
        app['robot'] = app_loop.run_until_complete(sdk_conn.wait_for_robot())
    except cozmo.ConnectionError as e:
        sys.exit("A connection error occurred: %s" % e)

    web.run_app(app, host='0.0.0.0', port=5001)
