# Control System Interview Exercise
We've prepared an exercise to help with the technical evaluation portion of our interview process, while also providing an idea of the data that you'd be dealing with on a day-to-day basis. We also use this exercise to facilitate a discussion during the on-site interview process, so please come prepared to discuss your solution to the exercise in more detail.

## Exercise
You are given a CSV file with two columns. The first column is a timestamp, and the second column is a kWh value (a measurement of energy). Each row represents how much energy that has been consumed by the building in the 15-minute interval ending at the timestamp.

For example, ```"2015-01-01 00:00:00",8.899``` means 8.899 kWh has been consumed in the 15-minute interval starting at 2014-12-31 23:45:00 and ending at 2015-01-01 00:00:00.

Assume you are given a lithium-ion battery with 120kWh capacity. You can either lower the energy consumption of the building by discharging the battery, or increase the energy consumption by charging the battery.

Your first objective is to limit the energy consumption of the building at every 15-minute interval to a certain threshold. Find the lowest threshold that you can set for every month.

Assumptions for the first objective:
* Threshold resets at the beginning of each month.
* Battery charge level resets to 100% at the beginning of each month.
* The battery can either be charged, discharged, or stay idle during every 15-minute interval.
* There is no limit on the charge/discharge rate.
* Don't worry about charge/discharge inefficiencies.


Your second objective is to find the size of the lithium-ion battery that is needed to maintain a constant threshold of 18 kW.

Assumptions for the second objective:
* Battery charge level starts at 100%.
* The battery can either be charged, discharged, or stay idle during every 15-minute interval.
* There is no limit on the charge/discharge rate.
* Don't worry about charge/discharge inefficiencies.

We prefer the use of Python for this exercise, which is a focus for this role, however feel free to use another language for your solution if you feel more comfortable or feel that you can provide a more robust solution.  Feel free to use any additional tools/frameworks/libraries that you feel best fit the solution.

Please also provide an additional notes or details needed to setup or run your submission.

## Output

Please output the first objective to a CSV file named 'minimum_threshold.csv' using the same format provided in 'sample_output.csv'.  Output the second objective to a CSV file named 'minimum_capacity.csv' using the same format provided in 'sample_output.csv' except the results should be provided as a whole number.

## Communication

We’re big on communication and want to help you out in any way we can.

* **Slack** - We use Slack for team communication and we think it’s great.  We’ll invite you to a Slack channel you can use to ask us questions or follow-up on anything related to the interview or assignment.

* **Gitlab** - We use Gitlab for source control so we’ll share out a Gitlab repo that you should use to source control any code, wiki notes or other information you might use as part of your research.  Feel free to commit often as you work through the problem.

## Next Steps

We’ll be in contact with you and will setup a follow-up onsite interview within the next two weeks (depending on your availability and schedule).  Before you come in for the on-site interview, please push your results to GitLab including an updated README with any additional instructions we may need to run any code.   Also, please list any tools/programming languages/etc you are using so that we can be prepared for the onsite interview.  When you come on-site, we will provide you some feedback and have a discussion about your approach, and there may also be some interactive coding and analysis that we’ll work through with you.

If you have any questions at any time please email us, call us, or message us on Slack!
