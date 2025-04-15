def declaration_to_lean(declaration):
    """
    将Declaration转换为Lean代码格式
    
    参数:
    declaration (tuple): 包含variable和ConceptID的元组 (variable, concept_id)
    
    返回:
    str: 转换后的Lean代码声明
    """
    if len(declaration) != 2:
        raise ValueError("Declaration must be a tuple of (variable, concept_id)")
    
    variable, concept_id = declaration

        # 根据不同的ConceptID进行匹配
    if concept_id == "Real":
        return f"({variable} : ℝ)"
    elif concept_id == "Nat":
        return f"({variable} : ℕ)"
    elif concept_id == "Int":
        return f"({variable} : ℤ)"
    elif concept_id == "Bool":
        return f"({variable} : 𝔹)"
    elif concept_id == "Set":
        return f"({variable} : Set)"
    elif concept_id == "Function":
        return f"({variable} : Function)"
    elif concept_id == "Vector":
        return f"({variable} : Vector)"
    elif concept_id == "Matrix":
        return f"({variable} : Matrix)"
    elif concept_id == "Prime":
        return f"(Prime {variable})"
    elif concept_id == "Even":
        return f"(Even {variable})"
    elif concept_id == "Odd":
        return f"(Odd {variable})"
    elif concept_id == "Positive":
        return f"({variable} > 0)"
    elif concept_id == "Negative":
        return f"({variable} < 0)"
    elif concept_id == "NonNegative":
        return f"({variable} ≥ 0)"
    elif concept_id == "NonPositive":
        return f"({variable} ≤ 0)"
    else:
        # 默认处理，直接使用ConceptID作为类型
        return f"({variable} : {concept_id})"
    
# 实数声明
print(declaration_to_lean(("x", "Real")))  # 输出: (x : ℝ)

# 自然数声明
print(declaration_to_lean(("n", "Nat")))   # 输出: (n : ℕ)

# 正数声明
print(declaration_to_lean(("y", "Positive")))  # 输出: (y > 0)

# 自定义类型声明
print(declaration_to_lean(("f", "MyType")))   # 输出: (f : MyType)