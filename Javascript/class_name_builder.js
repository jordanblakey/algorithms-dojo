class nameBuilder{
  // Given a first name, a last name, or both, return a string with the fullest name possible
  constructor(fn,ln){
    this.fn=fn,this.ln=ln
  }
  getFullName(){
    return(!this.ln)?this.fn:
    (!this.fn)?this.ln: 
    this.fn+' '+this.ln
  }
}
