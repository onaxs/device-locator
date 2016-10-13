from flask import Flask, render_template
from pyicloud import PyiCloudService

api = PyiCloudService('sweeting.xano@gmail.com')
app =  Flask(__name__)


@app.route('/')
def get_iphone():
	devices = api.devices
	iphone = devices['tsW0bdWVmfu6Tk98xwM5kNCAay80OLAc1QvNCuNWt1L+K+OqiwEIGuHYVNSUzmWV'] 
	location = iphone.location()

	return render_template(
		'devices.html',
		name=iphone.data['name'],
		latitude=location['latitude'],
		longitude=location['longitude'],
	)


if __name__ == '__main__':
	app.run(debug=True)