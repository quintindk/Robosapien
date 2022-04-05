from flask import Flask
from flask import request
from flask import Response
import json
import robo

command_codes={
  "CONTROL_WakeUp" : 0xB1,
  "CONTROL_Listen" : 0xAB,
  "CONTROL_Reset" : 0xAE,
  "CONTROL_PowerOff" : 0xD1,
  "CONTROL_Sleep" : 0xA3,
  "CONTROL_NoOp" : 0xEF,

  "PLAY_Execute" : 0xB0,
  "PLAY_RightSensor" : 0xB2,
  "PLAY_LeftSensor" : 0xB3,
  "PLAY_SonicSensor" : 0xB4,
  "PLAY_AllDemo" : 0xD0,
  "PLAY_Demo1" : 0xD2,
  "PLAY_Demo2" : 0xD3,
  "PLAY_Dance" : 0xD4,
  "PLAY_Roar" : 0xCE,
  "PLAY_FeetShuffle" : 0xF6,
  "PLAY_RaiseArmThrow" : 0xFC,
  "PLAY_KarateChop" : 0xD6,

  "MOVE_TurnRight" : 0x80,
  "MOVE_RightArmUp" : 0x81,
  "MOVE_RightArmOut" : 0x82,
  "MOVE_TiltBodyRight" : 0x83,
  "MOVE_RightArmDown" : 0x84,
  "MOVE_RightArmIn" : 0x85,
  "MOVE_WalkForward" : 0x86,
  "MOVE_WalkBackward" : 0x87,
  "MOVE_TurnLeft" : 0x88,
  "MOVE_LeftArmUp" : 0x89,
  "MOVE_LeftArmOut" : 0x8A,
  "MOVE_TiltBodyLeft" : 0x8B,
  "MOVE_LeftArmDown" : 0x8C,
  "MOVE_LeftArmIn" : 0x8D,
  "MOVE_Stop" : 0x8E,
  "MOVE_Burp" : 0xC2,
  "MOVE_RightHandStrike" : 0xC0,

  "PROG_MasterCommand" : 0x90,
  "PROG_Play" : 0x91,
  "PROG_RightSensor" : 0x92,
  "PROG_LeftSensor" : 0x93,
  "PROG_SonicSensor" : 0x94,

  "MOVE_RightTurnStep" : 0xA0,
  "MOVE_RightHandThump" : 0xA1,
  "MOVE_RightHandThrow" : 0xA2,

  "MOVE_RightHandPickup" : 0xA4,
  "MOVE_LeanBackward" : 0xA5,
  "MOVE_ForwardStep" : 0xA6,
  "MOVE_BackwardStep" : 0xA7,
  "MOVE_LeftTurnStep" : 0xA8,
  "MOVE_LeftHandThump" : 0xA9,
  "MOVE_LeftHandThrow" : 0xAA,
  "MOVE_LeftHandPickup" : 0xAC,
  "MOVE_LeanForward" : 0xAD,

  "MOVE_RightHandStrike3" : 0xC0,
  "MOVE_RightHandSweep" : 0xC1,
  "MOVE_Burp" : 0xC2,
  "MOVE_RightHandStrike2" : 0xC3,
  "MOVE_High5" : 0xC4,
  "MOVE_RightHandStrike1" : 0xC5,
  "MOVE_Bulldozer" : 0xC6,
  "MOVE_Oops" : 0xC7,
  "MOVE_LeftHandStrike3" : 0xC8,
  "MOVE_LeftHandSweep" : 0xC9,
  "MOVE_Whistle" : 0xCA,
  "MOVE_LeftHandStrike2" : 0xCB,
  "MOVE_Talkback" : 0xCC,
  "MOVE_LeftHandStrike1" : 0xCD,
}

app=Flask(__name__)
@app.route('/')
def index():
  return 'Server Works!'


@app.route('/commands',methods = ['GET'])
def get_commands():
  return Response(json.dumps(command_codes, indent=2), status=200)

@app.route('/send',methods = ['POST', 'GET'])
def send_command():
  if (request.method == 'POST'):
    try:
      rs=robo.Robo(21)
      rs.send_code(command_codes[request.form['code_to_send']])
      return Response(status=200)
    except:
      return Response(status=402)

  return Response(json.dumps(command_codes, indent=2), status=200)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')