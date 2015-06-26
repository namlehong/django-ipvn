from django.db import models
import random


class IpRange(models.Model):
    from_ip = models.IPAddressField()
    to_ip = models.IPAddressField()

    def generate(self):
        start = list(map(int, self.from_ip.split(".")))
        end = list(map(int, self.to_ip.split(".")))

        temp = start
        for i in range(len(start)):
            if temp[i] < end[i]:
                temp[i] = random.randrange(start[i], end[i]+1)

        return ".".join(map(str, temp))