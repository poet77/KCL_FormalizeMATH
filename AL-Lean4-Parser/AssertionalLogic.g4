grammar AssertionalLogic;

// Parser rules
program
    : '{' 
      '"Declarations"' ':' '"' declarationList '"' ','?
      '"Facts"' ':' '"' factList '"' ','?
      '"Query"' ':' '"' query '"' ','?
      '"Proof"' ':' '"' proofList '"'?
      '}'
    | traditionalProgram
    ;

traditionalProgram
    : declarationList? factList? queryList? proofList? EOF
    ;

declarationList
    : declaration (';' declaration)*
    ;

declaration
    : variable ':' conceptID
    ;

factList
    : assertion (';' assertion)*
    ;

assertion
    : term '=' term
    ;

queryList
    : query (';' query)*
    ;

query
    : term '=' '?'
    ;

proofList
    : ('?' assertion (';' '?' assertion)*)?
    ;

terms
    : (declaration | term) (',' ( term | proposition))*
    ;


term
    : '(' term ')'                     # ParenTerm
    | term op=('*' | '/' | '%') term   # BinaryOpTerm
    | term op=('+' | '-') term         # BinaryOpTerm
    | operatorID '(' terms ')'         # OperatorTerm
    | atomicIndividual            # AtomicTerm
    ;


proposition
    : arithmeticExpression ('=' | '>' | '<') arithmeticExpression
    ;

arithmeticExpression
    : term ('+' | '-' | '*' | '/') term
    | term
    ;

atomicIndividual
    : constant
    | variableID
    ;

constant
    : numeral
    | logicalConstant
    | mathematicalConstant
    ;

conceptID
    : 'Real'
    | 'NonNegativeNumbers'
    | 'NegativeNumbers'
    | 'PositiveNumbers'
    | 'TranscendentalNumbers'
    | 'AlgebraicNumbers'
    | 'IrrationalNumbers'
    | 'Integers'
    | 'EvenNumbers'
    | 'OddNumbers'
    | 'PositiveIntegers'
    | 'NegativeIntegers'
    | 'NonNegativeIntegers'
    | 'NaturalNumbers'
    | 'PrimeNumbers'
    | 'CompositeNumbers'
    | 'RationalNumbers'
    | 'Decimals'
    | 'RepeatingDecimals'
    | 'ComplexNumbers'
    | 'ImaginaryNumbers'
    | 'Infinity'
    | 'PositiveInfinity'
    | 'NegativeInfinity'
    | 'Polynomial'
    | 'Monomial'
    | 'IrreduciblePolynomial'
    | 'QuadraticPolynomial'
    | 'CubicPolynomial'
    | 'Function'
    | 'QuadraticFunction'
    | 'CubicFunction'
    | 'Set'
    | 'Sequence'
    | 'ArithmeticSequence'
    | 'GeometricSequence'
    | 'HarmonicSequence'
    | 'Expression'
    | 'Equation'
    | 'Inequation'
    | 'Operator'
    | 'Number'
    ;

operatorID
    : 'Get_Number_Floor'
    | 'Get_Number_Ceil'
    | 'Get_Number_Round'
    | 'Abs'
    | 'Log'
    | 'NaturalLog'
    | 'Sqrt'
    | 'Factorial'
    | 'Get_Combination'
    | 'Get_Reciprocal'
    | 'Get_Sum'
    | 'Get_Prod'
    | 'Exp'
    | 'Solve_equation'
    | 'Solve_inequation'
    | 'Get_Value_Expression'
    | 'Get_PolyDegree'
    | 'Get_Polyroots'
    | 'Get_Term_Coefficient'
    | 'Get_PolyTerm'
    | 'Get_ConstantTerm'
    | 'IsPolyFactor'
    | 'Is_IrreduciblePolynomial'
    | 'Get_PolyCoefficient'
    | 'Eval_Value_Polynomial'
    | 'Is_Polynomial_Root'
    | 'Get_Polynomial_Composition'
    | 'Get_Polynomial_Leading_Coefficient'
    | 'Get_Sequence_Terms'
    | 'Get_Sequences_Sum'
    | 'Is_ArithmeticSequence'
    | 'Is_GeometricSequence'
    | 'Is_MonotonicSequence'
    | 'Get_CommonDifference'
    | 'Get_CommonRatio'
    | 'Is_Monotonic_Increasing_Sequence'
    | 'Is_Monotonic_Decreasing_Sequence'
    | 'Get_FiniteSequences_Length'
    | 'Get_Sequence_Infinite_Sum'
    | 'Get_Function_Range'
    | 'Get_Function_Maximum'
    | 'Get_Function_Minimum'
    | 'Get_Function_Symmetry'
    | 'Get_Function_Zeroes'
    | 'Get_Function_Composition'
    | 'Get_Function_Minimalperiod'
    | 'Get_Inverse_Function'
    | 'Get_Function_IthComposition'
    | 'Get_Function_Value'
    | 'Is_Bijection'
    | 'Is_Injection'
    | 'Is_Surjection'
    | 'Get_QuadraticFunction_Discriminant'
    | 'Get_Function_Expression'
    | 'Get_StepFunction_Expression'
    | 'Is_Function_Root'
    | 'Get_Function_InDomain_Range'
    | 'Set_Union'
    | 'Set_Intersection'
    | 'Set_Difference'
    | 'Set_SymmetricDifference'
    | 'Set_Subset'
    | 'Set_ProperSubset'
    | 'Set_Superset'
    | 'Set_ProperSuperset'
    | 'Set_Cardinality'
    | 'Set_PowerSet'
    | 'Set_Complement'
    | 'Set_Equality'
    | 'Get_Set_Sum'
    | 'Get_Set_Product'
    | 'Build_Set'
    | 'Get_Set_Maximum'
    | 'Get_Set_Minimum'
    | 'Elements_In_Set'
    | 'Get_Set_Means'
    | 'Is_Set_BoundedFromAbove'
    | 'Is_Set_Unbounded'
    | 'Get_UniversalSet'
    | 'Range'
    | 'Get_Open_Interval'
    | 'Get_LeftClosedRightOpen_Interval'
    | 'Get_LeftOpenRightClosed_Interval'
    | 'Get_Closed_Interval'
    | 'Get_RightOpen_Interval'
    | 'Get_RightClosed_Interval'
    | 'Get_LeftOpen_Interval'
    | 'Get_LeftClosed_Interval'
    | 'Negation'
    | 'Build_Universal_Proposition'
    | 'Build_Exist_Proposition'
    | 'And'
    | 'Or'
    | 'Implication'
    | 'Equivalence'
    | 'Build_UniqueExist_Proposition'
    | 'Get_Angle_DegreeMeasure'
    | 'Get_Angle_RadianMeasure'
    | 'Change_Degree_To_Radian'
    | 'Change_Radian_To_Degree'
    | 'Sin'
    | 'Cos'
    | 'Tan'
    | 'Cot'
    | 'Is_Odd_Number'
    | 'Is_Even_Number'
    | 'Is_Prime_Number'
    | 'Is_Composite'
    | 'Get_FractionalPart'
    | 'Get_IntegerPart'
    | 'Get_LeastCommonDenominator'
    | 'Get_Mediant'
    | 'UnitFraction'
    | 'Is_ProperFraction'
    | 'Is_IrreducibleFraction'
    | 'Is_Coprime'
    | 'Is_Factor'
    | 'Get_GCD'
    | 'Get_LCM'
    | 'Is_PerfectSquare'
    | 'Get_Remainder'
    | 'Is_Prime'
    | 'Get_SumOfSquares'
    | 'Is_Twin_Prime'
    | 'Is_Factorial_Prime'
    | 'Is_MersenneNumber'
    | 'Is_SinglyEvenNumber'
    | 'Order'
    | 'Get_Mod_Nat'
    | 'Is_Nat_Mod'
    | atomicOperator 
    ;

atomicOperator
    : '+' | '-' | '*' | '/' | '%'  // Basic arithmetic operators
    ;


// Lexer rules
variable
    : LOWERCASE_LETTER (LOWERCASE_LETTER)*
    ;

variableID
    : LOWERCASE_LETTER (LOWERCASE_LETTER)*
    ;

numeral
    : DIGIT+                      # Integer
    | DIGIT+ '.' DIGIT+           # Float
    ;

logicalConstant
    : 'True'
    | 'False'
    ;

mathematicalConstant
    : 'pi'
    | 'e'
    | 'i'
    ;

// Basic tokens
UPPERCASE_LETTER: [A-Z];
LOWERCASE_LETTER: [a-z];
ALPHABET: [A-Za-z];
DIGIT: [0-9];

// Operators and punctuation
QUESTION: '?';
COLON: ':';
COMMA: ',';
SEMICOLON: ';';
LPAREN: '(';
RPAREN: ')';
UNDERSCORE: '_';

// Whitespace and comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '--' ~[\r\n]* -> skip;





// Predefined Concept Keywords
REAL: 'Real';
NON_NEGATIVE_NUMBERS: 'NonNegativeNumbers';
NEGATIVE_NUMBERS: 'NegativeNumbers';
POSITIVE_NUMBERS: 'PositiveNumbers';
TRANSCENDENTAL_NUMBERS: 'TranscendentalNumbers';
ALGEBRAIC_NUMBERS: 'AlgebraicNumbers';
IRRATIONAL_NUMBERS: 'IrrationalNumbers';
INTEGERS: 'Integers';
EVEN_NUMBERS: 'EvenNumbers';
ODD_NUMBERS: 'OddNumbers';
POSITIVE_INTEGERS: 'PositiveIntegers';
NEGATIVE_INTEGERS: 'NegativeIntegers';
NON_NEGATIVE_INTEGERS: 'NonNegativeIntegers';
NATURAL_NUMBERS: 'NaturalNumbers';
PRIME_NUMBERS: 'PrimeNumbers';
COMPOSITE_NUMBERS: 'CompositeNumbers';
RATIONAL_NUMBERS: 'RationalNumbers';
DECIMALS: 'Decimals';
REPEATING_DECIMALS: 'RepeatingDecimals';
COMPLEX_NUMBERS: 'ComplexNumbers';
IMAGINARY_NUMBERS: 'ImaginaryNumbers';
INFINITY: 'Infinity';
POSITIVE_INFINITY: 'PositiveInfinity';
NEGATIVE_INFINITY: 'NegativeInfinity';
POLYNOMIAL: 'Polynomial';
MONOMIAL: 'Monomial';
IRREDUCIBLE_POLYNOMIAL: 'IrreduciblePolynomial';
QUADRATIC_POLYNOMIAL: 'QuadraticPolynomial';
CUBIC_POLYNOMIAL: 'CubicPolynomial';
FUNCTION: 'Function';
QUADRATIC_FUNCTION: 'QuadraticFunction';
CUBIC_FUNCTION: 'CubicFunction';
SET: 'Set';
SEQUENCE: 'Sequence';
ARITHMETIC_SEQUENCE: 'ArithmeticSequence';
GEOMETRIC_SEQUENCE: 'GeometricSequence';
HARMONIC_SEQUENCE: 'HarmonicSequence';
EXPRESSION: 'Expression';
EQUATION: 'Equation';
INEQUATION: 'Inequation';
OPERATOR: 'Operator';
NUMBER: 'Number';
