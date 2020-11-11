from nw_products import NorthwindProducts  # Importing the class we want to run methods from


class Runner(NorthwindProducts):
    # We only need to run the avg_val() method so lets return what's returned from the avg_val() method
    def run_avg_val(self):
        return super().avg_val()


# Creating an instance and running our method
test = Runner()
print(test.run_avg_val())
