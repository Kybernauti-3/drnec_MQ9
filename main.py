from lib import MQ

mq = MQ()
perc = mq.MQPercentage()
print("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))