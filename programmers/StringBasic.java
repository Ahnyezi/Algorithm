package programmers;

public class StringBasic {
	public boolean solution2(String s) {
	      if(s.length() == 4 || s.length() == 6){
	          try{
	              int x = Integer.parseInt(s);
	              return true;
	          } catch(NumberFormatException e){
	              return false;
	          }
	      }
	      else return false;
	  }

	public boolean solution(String s) {
	       boolean flag = false;
			char[] str = s.toCharArray();
			if (str.length==4||str.length==6){
				for(char i: str){
					if(Character.isDigit(i)) flag = true;
					else if (Character.isAlphabetic(i)){
						flag = false;
						break; //헷갈린 부분: 앞이 문자인경우
					}
				}
			}
			return flag;
	    }

}
