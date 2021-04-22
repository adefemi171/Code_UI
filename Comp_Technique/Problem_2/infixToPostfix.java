import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;
import java.util.regex.*;

public class infixToPostFix {

    private static Pattern digitMatcher = Pattern.compile("[0-9\\.]+");
    private static Pattern operatorMatcher = Pattern.compile("[+\\-/*()^]");

    private static boolean charMatchesRegex(Pattern pattern, char value) {
        return pattern.matcher(String.valueOf(value)).matches();
    }


    private static String[] tokenizer(String input) throws Exception {
        ArrayList<String> tokens = new ArrayList<>();
        char[] inputCharArray = input.toCharArray();
        int cursor = 0;
        while (cursor < inputCharArray.length) {
            if (inputCharArray[cursor] == ' ') {
                cursor++;
                continue;
            }
//           check for digit
            if (charMatchesRegex(digitMatcher, inputCharArray[cursor])) {
                String buffer = "";
                int index = cursor;
                while (index < inputCharArray.length && charMatchesRegex(digitMatcher, inputCharArray[index])) {
                    buffer += inputCharArray[index];
                    index++;
                }
                tokens.add(buffer);
                cursor = index;
                continue;
            }

//            check for operator
            if (charMatchesRegex(operatorMatcher, inputCharArray[cursor]) && cursor < inputCharArray.length) {
                tokens.add(String.valueOf(inputCharArray[cursor]));
                cursor++;
                continue;
            }

            throw new Exception("Invalid expression");
        }
        String[] tokensArray = new String[tokens.size()];
        for (int j = 0; j < tokens.size(); j++) {
            tokensArray[j] = tokens.get(j);
        }
        return tokensArray;
    }

    static int precedence(char c) {
        switch (c) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '^':
                return 3;
        }
        return -1;
    }

    static String[] infixToPostFix(String[] expression) {

        ArrayList<String> result = new ArrayList<>();
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < expression.length; i++) {
            String c = expression[i];

            if (precedence(c.charAt(0)) > 0) {
                while (stack.isEmpty() == false && precedence(stack.peek().charAt(0)) >= precedence(c.charAt(0))) {
                    result.add(stack.pop());
                }
                stack.push(c);
            } else if (c.equals(")")) {
                String x = stack.pop();
                while (!x.equals("(")) {
                    result.add(x);
                    x = stack.pop();
                }
            } else if (c.equals("(")) {
                stack.push(c);
            } else {
                //character is neither operator nor (
                result.add(c);
            }
        }
        for (int i = 0; i <= stack.size(); i++) {
            result.add(stack.pop());
        }

        String[] returning = new String[result.size()];
        for (int i = 0; i < returning.length; i++) {
            returning[i] = result.get(i);
        }
        return returning;
    }

    static float operate( String operator , Stack<String> stack){
        float a = Float.parseFloat(stack.pop());
        float b = Float.parseFloat(stack.pop());
        switch (operator) {
            case "+":
                return b + a;
            case "-":
                return b - a;
            case "*":
                return b * a;
            case "/":
                return b / a;
            default:
                return 0;
        }
    }

    static float solvePostfix(String[] postFixExpression) {
        Stack<String> solutionStack = new Stack<>();
//        populate stack
        int i = 0;
        while (i < postFixExpression.length) {
            if(operatorMatcher.matcher(postFixExpression[i]).matches()){
                Float soln = operate(postFixExpression[i] , solutionStack);
                solutionStack.push(soln.toString());
                i++;
                continue;
            }
            solutionStack.push(postFixExpression[i]);
            i++;
            continue;

        }

        return Float.parseFloat(solutionStack.pop());
    }

    public static void main(String[] args) {
        try {

            System.out.println("Enter expression ==>");
            Scanner scan = new Scanner(System.in);
            String val = scan.nextLine();
            String[] tokens = tokenizer(val);
            System.out.print("tokens ==> ");
            for (String i : tokens) {
                System.out.print(i);
                System.out.print(" ");
            }
            System.out.println("");

            String[] postFix = infixToPostFix(tokens);
            System.out.print("Postfix ==> ");
            for (String i : postFix) {
                System.out.print(i);
                System.out.print(" ");
            }
            System.out.println("");
            System.out.println("Solution ==> " + solvePostfix(postFix));
        } catch (Exception er) {
            er.printStackTrace();
        }
    }
}
