function numberToEnglish(n){
  // Write a method that takes a number and returns a string of that number in English. For example
  // numberToEnglish(27) // => 'twenty seven'
  // Your method should be able to handle any number between 0 and 99999. If given numbers outside of that range or non-Integer numbers, the method should return an empty string.

  // DICTIONARIES ///////////////////////////////////////////////////
  let ones = { '0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine' }
  let tens = { '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen', '2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety', }

  // INIT ///////////////////////////////////////////////////////////
  console.log('Original n:',n,'\n==BEGIN====================')
  if (n%1!=0 || n < 0) return '' // Check is int
  n=n.toString().split('').map(Number)
  let l=n.length,eng='',bail=false,on=n.slice()
  let fmt=()=>eng.trim().replace('  ',' ').replace('  ',' ').replace('  ',' ')
  
  
  // MAIN LOOP //////////////////////////////////////////////////////
  for (i=0; i<on.length; i++){
    l=n.length // update length
    console.log('n:',n,'| l:',l,'| i:',i, '| on[i]:',on[i] ); // status update
    // console.log('n[i]!!!', n[i])
    console.log('>>> n[0]:', n[0]);
    // console.log('n[1]!!!', n[1]);

    console.log(n.slice(1))
    if (l>1 && n.slice(0).reduce((p,c)=>p+c==0)){bail=true}
          
    // THREE DIGITS /////

    if (l>2 && n[0]!=0) {
      //console.log('OVER ONE HUNDRED')
      (l==5&&n[0]==1&&n[1]==0)?eng+='ten':
      (l==5&&n[1]==0)?(eng+=tens[n[0]]): // twenty, thirty, forty
      (l==5&&n[0]==1)?((eng+=tens[n[0].toString()+n[1].toString()],n.shift())): // teens
      (l==5&&n[0]>=2)?(eng+=tens[n[0]]): // twenty
      eng+=ones[n[0]];
      
      (l==4||l==5&&n[1]==1||l==5&&n[1]==0)?eng+=' thousand':
      l==3?eng+=' hundred':null
    }
    // TWO DIGITS /////
    (l==2&&n[0]==1&&n[1]==0)?(eng+='ten', bail=true):
    (l==2&&n[1]==0)?(eng+=tens[n[0]], bail=true): // twenty, thirty, forty
    (l==2&&n[0]==1)?(eng+=tens[n[0].toString()+n[1].toString()], bail=true): // teens
    (l==2&&n[0]!=0)?eng+=tens[n[0]]: // 99 < n > twenty
    
    // ONE DIGIT //////
    l==1?eng+=ones[n]:null // ones  

    // POST ///////////
    l>1?n.shift():n=[] // move to next place
    console.log('n:', n, '| on[i]:',on[i],'| i:', i,'| eng:', fmt(),'| bail?', bail,'\n==LOOP END==================');
    (l!=1)?eng+=' ':null // space betreen words
    if(bail==true)return fmt() // check for exit
  }

  return fmt()
}

// TESTS
// Test.describe("Basic tests",_=>{
//   Test.it("should handle numbers between 0-99999",_=>{
//     Test.assertEquals(numberToEnglish(10), 'ten');
// 
//     Test.assertEquals(numberToEnglish(0), 'zero');
//     Test.assertEquals(numberToEnglish(7), 'seven');
//     Test.assertEquals(numberToEnglish(11), 'eleven');
//     Test.assertEquals(numberToEnglish(20), 'twenty');
//     Test.assertEquals(numberToEnglish(47), 'forty seven');
//     Test.assertEquals(numberToEnglish(100), 'one hundred');
//     Test.assertEquals(numberToEnglish(305), 'three hundred five');
//     Test.assertEquals(numberToEnglish(4002), 'four thousand two');
//     Test.assertEquals(numberToEnglish(3892), 'three thousand eight hundred ninety two');
//     Test.assertEquals(numberToEnglish(6800), 'six thousand eight hundred');
//     Test.assertEquals(numberToEnglish(14111), 'fourteen thousand one hundred eleven');
//     Test.assertEquals(numberToEnglish(20005), 'twenty thousand five');
//     Test.assertEquals(numberToEnglish(99999), 'ninety nine thousand nine hundred ninety nine');
//   })
//   Test.it("should return empty string when given number out of range or non integer",_=>{
//     Test.assertEquals(numberToEnglish(95.99), '');
//     Test.assertEquals(numberToEnglish(-4), '');
//   })    
// })
