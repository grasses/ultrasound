# About

Ultrasound是树莓派（Raspberry Pi）的一个超声波模块的包，主要功能超声波模块测距、速度，加速度。

(切记，先安装好树莓派GPIO环境)

------------------------

<br>

# Installation

### use pip

	pip install ultrasound

### or source install

	https://github.com/grasses/ultrasound/archive/master.zip
	
	unzip master.zip
	
	cd ultrasound-master
	
	python setup.py install
	
------------------------

<br>

# How to use

Package only can use BCM mode.

> GPIO.setmode(GPIO.BCM)

You can see as example:

	TRIG = 20
	ECHO = 21
	TIME_BREAK = 0.5

	def main( trig, echo, time_break ):
    	sensor = ultrasound.Ultrasound( trig, echo, time_break)
   	 	while True:
        	distance = int(sensor.get_distance())
        	print distance
        	time.sleep(0.04)
    
    if __name__ == "__main__":
    	trig = sys.argv[1] if len(sys.argv) > 1 else TRIG
    	echo = sys.argv[2] if len(sys.argv) > 2 else ECHO
    	time_break = sys.argv[3] if len(sys.argv) > 3 else ECHO
    	main(trig, echo, time_break)    
        
-------------------------------

<br>
  
# Warning      
  
* Only use in Raspberry Pi    
      
* Please install GPIO environment first (You can see here: [http://www.geekfan.net/8972/](http://www.geekfan.net/8972/))  
        

-------------------------------

<br>

# Version

14.10.27

* first version

15.03.27

* Solve the problem of stuck

* Improve running accuracy

15.04.02

* Update Version


-------------------------------

<br>

# License

### GPL        

        
        
        
        