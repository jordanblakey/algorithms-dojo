function evaporator(content, evap_per_day, threshold){ 

  // Given content(ml), evap per day(% of content), and replacement 
  //threshold(% of initial content), return the projected replacement day.

  let ev = evap_per_day / 100
  let evap_coefficient = 1 - ev
  let min = content - ((100 - threshold) / 100 * content)
  let day = 0

  console.log('\n== Initial Conditions ==============\n')  
  console.log('content in ml:', content)
  console.log('percentage evap per day:', ev)    
  console.log('precentage needed to function:', threshold + '%')
  console.log('minimum ml:', min)
  console.log('\n== Start Test ======================\n')

  while (content > min) {
    content = content * evap_coefficient
    day += 1
    console.log('day', day, '| ml:', content-min)
  }
  console.log('\n== Replacement Needed ==============\n== Current Day: '+day+' =================')
  return day
}


/* SAMPLE OUTPUT

== Initial Conditions ==============

content in ml: 10
percentage evap per day: 0.1
precentage needed to function: 10%
minimum ml: 1

== Start Test ======================

day 1 | ml: 8
day 2 | ml: 7.1
day 3 | ml: 6.29
day 4 | ml: 5.561
day 5 | ml: 4.9049000000000005
day 6 | ml: 4.3144100000000005
day 7 | ml: 3.7829690000000005
day 8 | ml: 3.3046721000000003
day 9 | ml: 2.8742048900000006
day 10 | ml: 2.4867844010000004
day 11 | ml: 2.1381059609000004
day 12 | ml: 1.8242953648100002
day 13 | ml: 1.541865828329
day 14 | ml: 1.2876792454961001
day 15 | ml: 1.05891132094649
day 16 | ml: 0.8530201888518409
day 17 | ml: 0.6677181699666568
day 18 | ml: 0.5009463529699911
day 19 | ml: 0.35085171767299195
day 20 | ml: 0.21576654590569277
day 21 | ml: 0.09418989131512356
day 22 | ml: -0.015229097816388815

== Replacement Needed ==============
== Current Day: 22 =================

Test Passed: Value == 22 */
