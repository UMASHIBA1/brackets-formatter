# coding: UTF-8

def formatter(raw_texts):
    formatted_text = ""
    tab_num = 0
    for raw_text in raw_texts:
        if raw_text == "(" or raw_text == "{" or raw_text == "[":
            tab_num += 1
            tab_str = "\t" * tab_num
            formatted_bracket = raw_text + "\n" + tab_str
            formatted_text += formatted_bracket
        elif raw_text == ")" or raw_text == "}" or raw_text == "]":
            tab_num -= 1
            tab_str = "\t" * tab_num
            formatted_bracket = "\n" + tab_str + raw_text
            formatted_text += formatted_bracket
        elif raw_text == ",":
            tab_str = "\t" * tab_num
            formatted_text += ",\n" + tab_str
        else:
            formatted_text += raw_text
    return formatted_text


# target_textにフォーマットしたい文字列を入れてください
target_text = """after visit_mut_with: Some(Decl(Var(VarDecl { span: Span { lo: BytePos(0), hi: BytePos(99), ctxt: #0 }, kind: "const", declare: false, decls: [VarDeclarator { span: Span { lo: BytePos(6), hi: BytePos(98), ctxt: #0 }, name: Ident(BindingIdent { id: Ident { span: Span { lo: BytePos(6), hi: BytePos(7), ctxt: #1 }, sym: Atom('x' type=inline), optional: false }, type_ann: None }), init: Some(Object(ObjectLit { span: Span { lo: BytePos(10), hi: BytePos(98), ctxt: #0 }, props: [Prop(Method(MethodProp { key: Ident(Ident { span: Span { lo: BytePos(47), hi: BytePos(52), ctxt: #0 }, sym: Atom('hello' type=inline), optional: false }), function: Function { params: [Param { span: Span { lo: BytePos(53), hi: BytePos(56), ctxt: #0 }, decorators: [], pat: Ident(BindingIdent { id: Ident { span: Span { lo: BytePos(53), hi: BytePos(56), ctxt: #2 }, sym: Atom('arg' type=inline), optional: false }, type_ann: None }) }], decorators: [], span: Span { lo: BytePos(0), hi: BytePos(0), ctxt: #0 }, body: Some(BlockStmt { span: Span { lo: BytePos(0), hi: BytePos(0), ctxt: #0 }, stmts: [Return(ReturnStmt { span: Span { lo: BytePos(0), hi: BytePos(0), ctxt: #0 }, arg: Some(Call(CallExpr { span: Span { lo: BytePos(0), hi: BytePos(0), ctxt: #0 }, callee: Expr(Call(CallExpr { span: Span { lo: BytePos(41), hi: BytePos(95), ctxt: #0 }, callee: Expr(Ident(Ident { span: Span { lo: BytePos(0), hi: BytePos(0), ctxt: #3 }, sym: Atom('_asyncToGenerator' type=dynamic), optional: false })), args: [ExprOrSpread { spread: None, expr: Fn(FnExpr { ident: None, function: Function { params: [], decorators: [], span: Span { lo: BytePos(41), hi: BytePos(95), ctxt: #0 }, body: Some(BlockStmt { span: Span { lo: BytePos(58), hi: BytePos(95), ctxt: #0 }, stmts: [Expr(ExprStmt { span: Span { lo: BytePos(68), hi: BytePos(89), ctxt: #0 }, expr: Call(CallExpr { span: Span { lo: BytePos(68), hi: BytePos(88), ctxt: #0 }, callee: Expr(Member(MemberExpr { span: Span { lo: BytePos(68), hi: BytePos(79), ctxt: #0 }, obj: Expr(Ident(Ident { span: Span { lo: BytePos(68), hi: BytePos(75), ctxt: #1 }, sym: Atom('console' type=inline), optional: false })), prop: Ident(Ident { span: Span { lo: BytePos(76), hi: BytePos(79), ctxt: #0 }, sym: Atom('log' type=inline), optional: false }), computed: false })), args: [ExprOrSpread { spread: None, expr: Lit(Str(Str { span: Span { lo: BytePos(80), hi: BytePos(87), ctxt: #0 }, value: Atom('Hello' type=inline), has_escape: false, kind: Normal { contains_quote: true } })) }], type_args: None }) })] }), is_generator: true, is_async: false, type_params: None, return_type: None } }) }], type_args: None })), args: [], type_args: None })) })] }), is_generator: false, is_async: false, type_params: None, return_type: None } }))] })), definite: false }] })))"""

print(formatter(target_text))
