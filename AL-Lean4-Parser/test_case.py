from Operators import operator_id
import unittest

class TestOperators(unittest.TestCase):
    
    def test_Solve_inequation(self):
        result = operator_id("Solve_inequation", "x : Real", "x + 1 > 0")
        self.assertEqual(result, "{ x : Real | x + 1 > 0 }")
        
    def test_Abs(self):
        result = operator_id("Abs", "x")
        self.assertEqual(result, "(|x|)")
        
    def test_Get_Number_Floor(self):
        result = operator_id("Get_Number_Floor", "3.7")
        self.assertEqual(result, "⌊(3.7: Real)⌋")
        
    def test_Get_Number_Ceil(self):
        result = operator_id("Get_Number_Ceil", "3.2")
        self.assertEqual(result, "⌈(3.2: Real)⌉")
        
    def test_Get_Number_Round(self):
        result = operator_id("Get_Number_Round", "3.5")
        self.assertEqual(result, "round ((3.5: Real))")
        
    def test_Log(self):
        result = operator_id("Log", "2", "8")
        self.assertEqual(result, "Real.logb 2 8")
        
    def test_NaturalLog(self):
        result = operator_id("NaturalLog", "10")
        self.assertEqual(result, "Real.log 10")
        
    def test_Factorial(self):
        result = operator_id("Factorial", "5")
        self.assertEqual(result, "Nat.factorial 5")
        
    def test_Get_Combination(self):
        result = operator_id("Get_Combination", "5", "2")
        self.assertEqual(result, "5.choose 2")
        
    def test_Get_Reciprocal(self):
        result = operator_id("Get_Reciprocal", "4")
        self.assertEqual(result, "4⁻¹")
        
    def test_Get_Sum(self):
        result = operator_id("Get_Sum", "S", "i", "i^2")
        self.assertEqual(result, "(∑ i ∈ S, i^2)")
        
    def test_Get_Prod(self):
        result = operator_id("Get_Prod", "S", "i", "i^2")
        self.assertEqual(result, "(∏ i ∈ S, i^2)")
        
    def test_Exp(self):
        result = operator_id("Exp", "2")
        self.assertEqual(result, "exp 2")
        
    def test_Get_PolyDegree(self):
        result = operator_id("Get_PolyDegree", "p")
        self.assertEqual(result, "p.degree")
        
    def test_Get_Polyroots(self):
        result = operator_id("Get_Polyroots", "p")
        self.assertEqual(result, "p.roots")
        
    def test_Get_Term_Coefficient(self):
        result = operator_id("Get_Term_Coefficient", "p", "2")
        self.assertEqual(result, "p.coeff 2")
        
    def test_Get_PolyTerm(self):
        result = operator_id("Get_PolyTerm", "p")
        self.assertEqual(result, "monomial 2 (p.coeff 2)")
        
    def test_Get_ConstantTerm(self):
        result = operator_id("Get_ConstantTerm", "p")
        self.assertEqual(result, "p.coeff 0")
        
    def test_Is_PolyFactor(self):
        result = operator_id("Is_PolyFactor", "p", "q")
        self.assertEqual(result, "p ∣ q")
        
    def test_Is_IrreduciblePolynomial(self):
        result = operator_id("Is_IrreduciblePolynomial", "p")
        self.assertEqual(result, "Irreducible p")
        
    def test_Get_PolyCoefficient(self):
        result = operator_id("Get_PolyCoefficient", "p")
        self.assertEqual(result, "p.coeffs")
        
    def test_Eval_Value_Polynomial(self):
        result = operator_id("Eval_Value_Polynomial", "p", "10")
        self.assertEqual(result, "eval 10 p")
        
    def test_Solve_equation(self):
        result = operator_id("Solve_equation", "x", "x + 1 = 0")
        self.assertEqual(result, "{ x | x + 1 = 0 }")
        
    def test_Is_Polynomial_Root(self):
        result = operator_id("Is_Polynomial_Root", "p", "a")
        self.assertEqual(result, "IsRoot p a")
        
    def test_Get_Polynomial_Composition(self):
        result = operator_id("Get_Polynomial_Composition", "f", "g")
        self.assertEqual(result, "comp f g")
        
    def test_Get_Polynomial_Leading_Coefficient(self):
        result = operator_id("Get_Polynomial_Leading_Coefficient", "p")
        self.assertEqual(result, "p.leadingCoeff")
        
    def test_Get_Sequence_Terms(self):
        result = operator_id("Get_Sequence_Terms", "seq", "10")
        self.assertEqual(result, "seq 10")
        
    def test_Get_Sequences_Sum(self):
        result = operator_id("Get_Sequences_Sum", "seq", "10")
        self.assertEqual(result, "∑ n ∈ Finset.Icc 1 10, seq n")
        
    def test_Is_ArithmeticSequence(self):
        result = operator_id("Is_ArithmeticSequence", "seq")
        self.assertEqual(result, "∃ d : ℝ, ∀ n : ℕ, seq (n + 1) - seq n = d")
        
    def test_Is_GeometricSequence(self):
        result = operator_id("Is_GeometricSequence", "seq")
        self.assertEqual(result, "∃ q : ℝ, ∀ n : ℕ, seq (n + 1) / seq n = q")
        
    def test_Is_MonotonicSequence(self):
        result = operator_id("Is_MonotonicSequence", "seq")
        self.assertEqual(result, "Monotone seq ∨ Antitone seq")
        
    def test_Get_CommonDifference(self):
        result = operator_id("Get_CommonDifference", "S")
        self.assertEqual(result, "S.d")

        # 单调序列测试
    def test_Is_Monotonic_Increasing_Sequence(self):
        result = operator_id("Is_Monotonic_Increasing_Sequence", "seq")
        self.assertEqual(result, "StrictMonoOn seq")
        with self.assertRaises(ValueError):
            operator_id("Is_Monotonic_Increasing_Sequence")  # 无参数
        with self.assertRaises(ValueError):
            operator_id("Is_Monotonic_Increasing_Sequence", "seq", "extra")  # 多余参数
    
    def test_Is_Monotonic_Decreasing_Sequence(self):
        result = operator_id("Is_Monotonic_Decreasing_Sequence", "seq")
        self.assertEqual(result, "StrictAntiOn seq")
    
    # 有限序列测试
    def test_Get_FiniteSequences_Length(self):
        result = operator_id("Get_FiniteSequences_Length", "seq")
        self.assertEqual(result, "seq.length")
    
    # 函数范围测试
    def test_Get_Function_Range(self):
        result = operator_id("Get_Function_Range", "f")
        self.assertEqual(result, "Set.range f")
    
    # 函数极值测试
    def test_Get_Function_Maximum(self):
        result = operator_id("Get_Function_Maximum", "f")
        self.assertEqual(result, "sSup (Set.range f)")
    
    def test_Get_Function_Minimum(self):
        result = operator_id("Get_Function_Minimum", "f")
        self.assertEqual(result, "sInf (Set.range f)")
    
    # 函数零点测试
    def test_Get_Function_Zeroes(self):
        result = operator_id("Get_Function_Zeroes", "f")
        self.assertEqual(result, "{ x | f x = 0 }")
    
    # 函数复合测试
    def test_Get_Function_Composition(self):
        result = operator_id("Get_Function_Composition", "f", "g")
        self.assertEqual(result, "f ∘ g")
        with self.assertRaises(ValueError):
            operator_id("Get_Function_Composition", "f")  # 缺少参数
    
    # 周期函数测试
    def test_Get_Function_Minimalperiod(self):
        result = operator_id("Get_Function_Minimalperiod", "f")
        self.assertEqual(result, "sInf {T: ℝ | T > 0 ∧ (∀ x, f (x + T) = f x)}")
    
    # 反函数测试
    def test_Get_Inverse_Function(self):
        result = operator_id("Get_Inverse_Function", "f")
        self.assertEqual(result, "f⁻¹")
    
    # 函数迭代测试
    def test_Get_Function_IthComposition(self):
        result = operator_id("Get_Function_IthComposition", "f", "3")
        self.assertEqual(result, "f^[3]")
    
    # 函数求值测试
    def test_Get_Function_Value(self):
        result = operator_id("Get_Function_Value", "f", "5")
        self.assertEqual(result, "f 5")
    
    # 函数性质测试
    def test_Is_Bijection(self):
        result = operator_id("Is_Bijection", "f")
        self.assertEqual(result, "Function.Bijective f")
    
    def test_Is_Injection(self):
        result = operator_id("Is_Injection", "f")
        self.assertEqual(result, "Function.Injective f")
    
    def test_Is_Surjection(self):
        result = operator_id("Is_Surjection", "f")
        self.assertEqual(result, "Function.Surjective f")
    
    # 二次函数测试
    def test_Get_QuadraticFunction_Discriminant(self):
        result = operator_id("Get_QuadraticFunction_Discriminant", "f")
        self.assertEqual(result, "f.discriminant")
    
    # 分段函数测试
    def test_Get_StepFunction_Expression(self):
        result = operator_id("Get_StepFunction_Expression", "f", "x > 2")
        expected = "theorem TestStepFunction (f: ℕ → ℕ)(h: ∀ x > 2, f x = x^2 + 1): f 3 = 10:= by\n  have h' : 3 > 2 :=by norm_num\n  exact h 3 h'"
        self.assertEqual(result, expected)
    
    # 集合运算测试
    def test_Set_Union(self):
        result = operator_id("Set_Union", "A", "B")
        self.assertEqual(result, "A ∪ B")
    
    def test_Set_Intersection(self):
        result = operator_id("Set_Intersection", "A", "B")
        self.assertEqual(result, "A ∩ B")
    
    def test_Set_Difference(self):
        result = operator_id("Set_Difference", "A", "B")
        self.assertEqual(result, "A \\ B")
    
    def test_Set_SymmetricDifference(self):
        result = operator_id("Set_SymmetricDifference", "A", "B")
        self.assertEqual(result, "symmDiff A B")
    
    # 集合关系测试
    def test_Set_Subset(self):
        result = operator_id("Set_Subset", "A", "B")
        self.assertEqual(result, "A ⊆ B")
    
    def test_Set_ProperSubset(self):
        result = operator_id("Set_ProperSubset", "A", "B")
        self.assertEqual(result, "A ⊂ B")
    
    def test_Set_Superset(self):
        result = operator_id("Set_Superset", "A", "B")
        self.assertEqual(result, "A ⊇ B")
    
    def test_Set_ProperSuperset(self):
        result = operator_id("Set_ProperSuperset", "A", "B")
        self.assertEqual(result, "A ⊃ B")
    
    # 集合属性测试
    def test_Set_Cardinality(self):
        result = operator_id("Set_Cardinality", "S")
        self.assertEqual(result, "S.card")
    
    def test_Set_PowerSet(self):
        result = operator_id("Set_PowerSet", "A")
        self.assertEqual(result, "𝒫 A")
    
    def test_Set_Complement(self):
        result = operator_id("Set_Complement", "A")
        self.assertEqual(result, "Aᶜ")
    
    def test_Set_Equality(self):
        result = operator_id("Set_Equality", "A", "B")
        self.assertEqual(result, "A = B")
    
    # 集合运算结果测试
    def test_Get_Set_Sum(self):
        result = operator_id("Get_Set_Sum", "S")
        self.assertEqual(result, "∑ i ∈ S, i")
    
    def test_Get_Set_Product(self):
        result = operator_id("Get_Set_Product", "S")
        self.assertEqual(result, "∏ i ∈ S, i")
    
    # 集合构造测试
    def test_Build_Set(self):
        result = operator_id("Build_Set", "x", "x > 2")
        self.assertEqual(result, "{x | x > 2}")

    # 集合极值和元素测试
    def test_Get_Set_Maximum(self):
        result = operator_id("Get_Set_Maximum", "A")
        self.assertEqual(result, "sSup A")
        with self.assertRaises(ValueError):
            operator_id("Get_Set_Maximum")  # 缺少参数
    
    def test_Get_Set_Minimum(self):
        result = operator_id("Get_Set_Minimum", "A")
        self.assertEqual(result, "sInf A")
    
    def test_Elements_In_Set(self):
        result = operator_id("Elements_In_Set", "x", "S")
        self.assertEqual(result, "x ∈ S")
        with self.assertRaises(ValueError):
            operator_id("Elements_In_Set", "x")  # 缺少参数
    
    # 集合统计测试
    def test_Get_Set_Means(self):
        result = operator_id("Get_Set_Means", "S")
        self.assertEqual(result, "(∑ i ∈ S, i )/(S.toFinset.card)")
    
    # 集合边界测试
    def test_Is_Set_BoundedFromAbove(self):
        result = operator_id("Is_Set_BoundedFromAbove", "A")
        self.assertEqual(result, "Set.Bounded Nat.le A")
    
    def test_Is_Set_Unbounded(self):
        result = operator_id("Is_Set_Unbounded", "A")
        self.assertEqual(result, "Set.Unbounded Nat.le A")
    
    # 全集测试
    def test_Get_UniversalSet(self):
        result = operator_id("Get_UniversalSet")
        self.assertEqual(result, "Set.univ")
        with self.assertRaises(ValueError):
            operator_id("Get_UniversalSet", "extra")  # 多余参数
    
    # 区间测试
    def test_Range(self):
        result = operator_id("Range", "1", "10")
        self.assertEqual(result, "Finset.Icc 1 10")
    
    def test_Get_Open_Interval(self):
        result = operator_id("Get_Open_Interval", "a", "b")
        self.assertEqual(result, "Set.Ioo a b")
    
    def test_Get_LeftClosedRightOpen_Interval(self):
        result = operator_id("Get_LeftClosedRightOpen_Interval", "1", "5")
        self.assertEqual(result, "Set.Ico 1 5")
    
    def test_Get_LeftOpenRightClosed_Interval(self):
        result = operator_id("Get_LeftOpenRightClosed_Interval", "0", "1")
        self.assertEqual(result, "Set.Ioc 0 1")
    
    def test_Get_Closed_Interval(self):
        result = operator_id("Get_Closed_Interval", "a", "b")
        self.assertEqual(result, "Set.Icc a b")
    
    def test_Get_RightOpen_Interval(self):
        result = operator_id("Get_RightOpen_Interval", "5")
        self.assertEqual(result, "Set.Iio 5")
    
    def test_Get_RightClosed_Interval(self):
        result = operator_id("Get_RightClosed_Interval", "10")
        self.assertEqual(result, "Set.Iic 10")
    
    def test_Get_LeftOpen_Interval(self):
        result = operator_id("Get_LeftOpen_Interval", "3")
        self.assertEqual(result, "Set.Ioi 3")
    
    def test_Get_LeftClosed_Interval(self):
        result = operator_id("Get_LeftClosed_Interval", "2")
        self.assertEqual(result, "Set.Ici 2")
    
    # 数字处理测试
    def test_Get_Digit(self):
        # 测试默认基数
        result = operator_id("Get_Digit", "123")
        self.assertEqual(result, "Nat.digits 10 123")
        # 测试指定基数
        result = operator_id("Get_Digit", "16", "255")
        self.assertEqual(result, "Nat.digits 16 255")
        # 测试错误参数
        with self.assertRaises(ValueError):
            operator_id("Get_Digit")  # 无参数
    
    def test_Covert_Digit_To_Number(self):
        result = operator_id("Covert_Digit_To_Number", "[1,2,3]")
        self.assertEqual(result, "Nat.ofDigits 10 [1,2,3]")
        result = operator_id("Covert_Digit_To_Number", "8", "[7,5]")
        self.assertEqual(result, "Nat.ofDigits 8 [7,5]")
    
    def test_Get_DigitCount(self):
        result = operator_id("Get_DigitCount", "100")
        self.assertEqual(result, "(Nat.digits 10 100).length")
        result = operator_id("Get_DigitCount", "2", "8")
        self.assertEqual(result, "(Nat.digits 2 8).length")
    
    def test_Get_DigitProduct(self):
        result = operator_id("Get_DigitProduct", "[1,2,3]")
        self.assertEqual(result, "List.foldl (λ (x:ℕ) (y:ℕ) => x * y) 1 [1,2,3]")
        result = operator_id("Get_DigitProduct", "10", "123")
        self.assertEqual(result, "List.foldl (λ (x:ℕ) (y:ℕ) => x * y) 1 (Nat.digits 10 123)")
    
    def test_Get_DigitSum(self):
        result = operator_id("Get_DigitSum", "[1,2,3]")
        self.assertEqual(result, "List.foldl (λ (x:ℕ) (y:ℕ) => x + y) 0 [1,2,3]")
    
    def test_Is_PandigitalNumber(self):
        result = operator_id("Is_PandigitalNumber", "digits")
        self.assertEqual(result, "(∀ d : ℕ, d ∈ (Finset.range 10) → d ∈ digits)")
    
    def test_Is_PalindromeNumber(self):
        result = operator_id("Is_PalindromeNumber", "12321")
        self.assertEqual(result, "(Nat.digits 10 12321).Palindrome")
    
    def test_Get_Ones_Digit(self):
        result = operator_id("Get_Ones_Digit", "123")
        self.assertEqual(result, "Nat.ofDigits 10 [(Nat.digits 10 123).head!]")
        result = operator_id("Get_Ones_Digit", "8", "64")
        self.assertEqual(result, "Nat.ofDigits 8 [(Nat.digits 8 64).head!]")
    
    # 数论测试
    def test_Is_Nat_Mod(self):
        result = operator_id("Is_Nat_Mod", "7", "3", "4")
        self.assertEqual(result, "7 ≡ 3 [MOD 4]")
    
    def test_Get_InverseMod(self):
        result = operator_id("Get_InverseMod", "3", "11")
        self.assertEqual(result, "∃ x : ℕ, 3 * x ≡ 1 [MOD 11]")
    
    def test_Get_FractionalPart(self):
        result = operator_id("Get_FractionalPart", "3.14")
        self.assertEqual(result, "Int.fract 3.14")
    
    def test_Get_IntegerPart(self):
        result = operator_id("Get_IntegerPart", "3.14")
        self.assertEqual(result, "Int.floor 3.14")
    
    def test_Get_LeastCommonDenominator(self):
        result = operator_id("Get_LeastCommonDenominator", "q1", "q2")
        self.assertEqual(result, "Nat.lcm q1.den q2.den")
    
    def test_Get_Mediant(self):
        result = operator_id("Get_Mediant", "q1", "q2")
        self.assertEqual(result, "(q1.num + q2.num) / (q1.den + q2.den)")
    
    def test_UnitFraction(self):
        result = operator_id("UnitFraction", "q")
        self.assertEqual(result, "(q.num = 1) ∧ (q.den > 0)")
    
    def test_Is_ProperFraction(self):
        result = operator_id("Is_ProperFraction", "q")
        self.assertEqual(result, "q.num < q.den")
    
    def test_Is_IrreducibleFraction(self):
        result = operator_id("Is_IrreducibleFraction", "q")
        self.assertEqual(result, "Int.gcd q.num q.den = 1")
    
    def test_Is_Coprime(self):
        result = operator_id("Is_Coprime", "8", "15")
        self.assertEqual(result, "Nat.Coprime 8 15")
    
    def test_Is_Factor(self):
        result = operator_id("Is_Factor", "3", "12")
        self.assertEqual(result, "3 ∣ 12")
    
    def test_Get_GCD(self):
        result = operator_id("Get_GCD", "12", "18")
        self.assertEqual(result, "Nat.gcd 12 18")
    
    def test_Get_LCM(self):
        result = operator_id("Get_LCM", "4", "6")
        self.assertEqual(result, "Nat.lcm 4 6")
    
    def test_Is_PerfectSquare(self):
        result = operator_id("Is_PerfectSquare", "16")
        self.assertEqual(result, "IsSquare 16")
    
    def test_Get_Remainder(self):
        result = operator_id("Get_Remainder", "7", "3")
        self.assertEqual(result, "7 % 3")
    
    def test_Is_Prime(self):
        result = operator_id("Is_Prime", "17")
        self.assertEqual(result, "Prime 17")
    
    def test_Get_SumOfSquares(self):
        result = operator_id("Get_SumOfSquares", "5")
        self.assertEqual(result, "∑ i ∈ Set.Icc 1 5, i ^ 2")
    
    def test_Is_Twin_Prime(self):
        result = operator_id("Is_Twin_Prime", "5")
        self.assertEqual(result, "Prime 5 ∧ (Prime (5 + 2) ∨ Prime (5 - 2))")
    
    def test_Is_Factorial_Prime(self):
        result = operator_id("Is_Factorial_Prime", "7")
        self.assertEqual(result, "Prime 7 ∧ (∃ n, 7 = Nat.factorial n + 1 ∨ 7 = Nat.factorial n - 1)")
    
    def test_Is_MersenneNumber(self):
        result = operator_id("Is_MersenneNumber", "31")
        self.assertEqual(result, "∃ n, 31 = 2 ^ n -1")
    
    def test_Is_SinglyEvenNumber(self):
        result = operator_id("Is_SinglyEvenNumber", "6")
        self.assertEqual(result, "2 ∣ 6 ∧ ¬ (4 ∣ 6)")
    
    def test_Order(self):
        result = operator_id("Order", "3", "7")
        self.assertEqual(result, "nat.orderOf 3 7")
        
    # 测试错误输入
    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            operator_id("Solve_inequation", "x > 0")  # 缺少参数
        with self.assertRaises(ValueError):
            operator_id("Abs", "x", "y")  # 多余参数
        with self.assertRaises(ValueError):
            operator_id("UnknownOperator", "x")  # 未知算子

if __name__ == "__main__":
    unittest.main()