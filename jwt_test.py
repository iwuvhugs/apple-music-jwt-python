import datetime
import jwt

keyId = "CapExedKid"
teamId = "CapExdTeam"
alg = 'ES256'

f = open("test_private_key.p8", "r")
secret = f.read()

time_now = datetime.datetime.now()
time_expired = datetime.datetime.now() + datetime.timedelta(hours=12)

headers = {
	"alg": alg,
	"kid": keyId
}

payload = {
	"iss": teamId,
	"exp": int(time_expired.strftime("%s")),
	"iat": int(time_now.strftime("%s"))
}


if __name__ == "__main__":
	"""Create an auth token"""
	token = jwt.encode(payload, secret, algorithm=alg, headers=headers)

	print "----TOKEN----"
	print token

	print "----CURL----"
	print "curl -v -H 'Authorization: Bearer %s' \"https://api.music.apple.com/v1/test\" " % (token)