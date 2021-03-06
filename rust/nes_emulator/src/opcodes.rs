use crate::cpu::AddressingMode;
use std::collections::HashMap;

pub struct OpCode {
    pub code: u8,
    pub mnemonic: &'static str,
    pub cycles: u8,
    pub mode: AddressingMode,
}

impl OpCode {
    pub fn new(code: u8, mnemonic: &'static str, cycles: u8, mode: AddressingMode) -> Self {
        OpCode {
            code: code,
            mnemonic: mnemonic,
            cycles: cycles,
            mode: mode,
        }
    }
}

lazy_static! {
    pub static ref CPU_OPS_CODES: Vec<OpCode> = vec![
        // AND
        OpCode::new(0x29, "AND", 2, AddressingMode::Immediate),
        OpCode::new(0x25, "AND", 3, AddressingMode::ZeroPage),
        OpCode::new(0x35, "AND", 4, AddressingMode::ZeroPageX),
        OpCode::new(0x2d, "AND", 4, AddressingMode::Absolute),
        OpCode::new(0x3d, "AND", 4, AddressingMode::AbsoluteX),
        OpCode::new(0x39, "AND", 4, AddressingMode::AbsoluteY),
        OpCode::new(0x21, "AND", 6, AddressingMode::IndirectX),
        OpCode::new(0x31, "AND", 5, AddressingMode::IndirectY),
        // Branches
        OpCode::new(0x90, "BCC", 2, AddressingMode::Immediate),
        OpCode::new(0xb0, "BCS", 2, AddressingMode::Immediate),
        OpCode::new(0xf0, "BEQ", 2, AddressingMode::Immediate),
        // BIT
        OpCode::new(0x24, "BIT", 3, AddressingMode::ZeroPage),
        OpCode::new(0x2c, "BIT", 4, AddressingMode::Absolute),
        // Branches
        OpCode::new(0x30, "BMI", 2, AddressingMode::Immediate),
        OpCode::new(0xd0, "BNE", 2, AddressingMode::Immediate),
        OpCode::new(0x10, "BPL", 2, AddressingMode::Immediate),
        //
        OpCode::new(0x00, "BRK", 1, AddressingMode::NoneAddressing),
        // Branches
        OpCode::new(0x50, "BVC", 2, AddressingMode::Immediate),
        OpCode::new(0x70, "BVS", 2, AddressingMode::Immediate),
        // CL*
        OpCode::new(0x18, "CLC", 2, AddressingMode::NoneAddressing),
        OpCode::new(0xd8, "CLD", 2, AddressingMode::NoneAddressing),
        OpCode::new(0x58, "CLI", 2, AddressingMode::NoneAddressing),
        OpCode::new(0xb8, "CLV", 2, AddressingMode::NoneAddressing),
        // CMP
        OpCode::new(0xc9, "CMP", 2, AddressingMode::Immediate),
        OpCode::new(0xc5, "CMP", 3, AddressingMode::ZeroPage),
        OpCode::new(0xd5, "CMP", 4, AddressingMode::ZeroPageX),
        OpCode::new(0xcd, "CMP", 4, AddressingMode::Absolute),
        OpCode::new(0xdd, "CMP", 4, AddressingMode::AbsoluteX),
        OpCode::new(0xd9, "CMP", 4, AddressingMode::AbsoluteY),
        OpCode::new(0xc1, "CMP", 6, AddressingMode::IndirectX),
        OpCode::new(0xd1, "CMP", 5, AddressingMode::IndirectY),
        // CPX
        OpCode::new(0xe0, "CPX", 2, AddressingMode::Immediate),
        OpCode::new(0xe4, "CPX", 3, AddressingMode::ZeroPage),
        OpCode::new(0xec, "CPX", 4, AddressingMode::Absolute),
        // CPY
        OpCode::new(0xc0, "CPY", 2, AddressingMode::Immediate),
        OpCode::new(0xc4, "CPY", 3, AddressingMode::ZeroPage),
        OpCode::new(0xcc, "CPY", 4, AddressingMode::Absolute),
        // DEC
        OpCode::new(0xc6, "DEC", 5, AddressingMode::ZeroPage),
        OpCode::new(0xd6, "DEC", 6, AddressingMode::ZeroPageX),
        OpCode::new(0xce, "DEC", 6, AddressingMode::Absolute),
        OpCode::new(0xde, "DEC", 7, AddressingMode::AbsoluteX),
        //
        OpCode::new(0xca, "DEX", 2, AddressingMode::NoneAddressing),
        OpCode::new(0x88, "DEY", 2, AddressingMode::NoneAddressing),
        // EOR
        OpCode::new(0x49, "EOR", 2, AddressingMode::Immediate),
        OpCode::new(0x45, "EOR", 3, AddressingMode::ZeroPage),
        OpCode::new(0x55, "EOR", 4, AddressingMode::ZeroPageX),
        OpCode::new(0x4d, "EOR", 4, AddressingMode::Absolute),
        OpCode::new(0x5d, "EOR", 4, AddressingMode::AbsoluteX),
        OpCode::new(0x59, "EOR", 4, AddressingMode::AbsoluteY),
        OpCode::new(0x41, "EOR", 6, AddressingMode::IndirectX),
        OpCode::new(0x51, "EOR", 5, AddressingMode::IndirectY),
        // INC
        OpCode::new(0xe6, "INC", 5, AddressingMode::ZeroPage),
        OpCode::new(0xf6, "INC", 6, AddressingMode::ZeroPageX),
        OpCode::new(0xee, "INC", 6, AddressingMode::Absolute),
        OpCode::new(0xfe, "INC", 7, AddressingMode::AbsoluteX),
        //
        OpCode::new(0xe8, "INX", 2, AddressingMode::NoneAddressing),
        OpCode::new(0xc8, "INY", 2, AddressingMode::NoneAddressing),
        // JMP
        OpCode::new(0x4c, "JMP", 3, AddressingMode::Absolute),
        OpCode::new(0x6c, "JMP", 3, AddressingMode::Indirect),
        // LDA
        OpCode::new(0xa9, "LDA", 2, AddressingMode::Immediate),
        OpCode::new(0xa5, "LDA", 3, AddressingMode::ZeroPage),
        OpCode::new(0xb5, "LDA", 4, AddressingMode::ZeroPageX),
        OpCode::new(0xad, "LDA", 4, AddressingMode::Absolute),
        OpCode::new(0xbd, "LDA", 4, AddressingMode::AbsoluteX),
        OpCode::new(0xb9, "LDA", 4, AddressingMode::AbsoluteY),
        OpCode::new(0xa1, "LDA", 6, AddressingMode::IndirectX),
        OpCode::new(0xb1, "LDA", 5, AddressingMode::IndirectY),
        // LDX
        OpCode::new(0xa2, "LDX", 2, AddressingMode::Immediate),
        OpCode::new(0xa6, "LDX", 3, AddressingMode::ZeroPage),
        OpCode::new(0xb6, "LDX", 4, AddressingMode::ZeroPageY),
        OpCode::new(0xae, "LDX", 4, AddressingMode::Absolute),
        OpCode::new(0xbe, "LDX", 4, AddressingMode::AbsoluteY),
        // LDY
        OpCode::new(0xa0, "LDY", 2, AddressingMode::Immediate),
        OpCode::new(0xa4, "LDY", 3, AddressingMode::ZeroPage),
        OpCode::new(0xb4, "LDY", 4, AddressingMode::ZeroPageX),
        OpCode::new(0xac, "LDY", 4, AddressingMode::Absolute),
        OpCode::new(0xbc, "LDY", 4, AddressingMode::AbsoluteX),
        // ORA
        OpCode::new(0x09, "ORA", 2, AddressingMode::Immediate),
        OpCode::new(0x05, "ORA", 3, AddressingMode::ZeroPage),
        OpCode::new(0x15, "ORA", 4, AddressingMode::ZeroPageX),
        OpCode::new(0x0d, "ORA", 4, AddressingMode::Absolute),
        OpCode::new(0x1d, "ORA", 4, AddressingMode::AbsoluteX),
        OpCode::new(0x19, "ORA", 4, AddressingMode::AbsoluteY),
        OpCode::new(0x01, "ORA", 6, AddressingMode::IndirectX),
        OpCode::new(0x11, "ORA", 5, AddressingMode::IndirectY),
        // S*
        OpCode::new(0x38, "SEC", 2, AddressingMode::NoneAddressing),
        OpCode::new(0xf8, "SED", 2, AddressingMode::NoneAddressing),
        OpCode::new(0x78, "SEI", 2, AddressingMode::NoneAddressing),
        // STA
        OpCode::new(0x85, "STA", 3, AddressingMode::ZeroPage),
        OpCode::new(0x95, "STA", 4, AddressingMode::ZeroPageX),
        OpCode::new(0x8d, "STA", 4, AddressingMode::Absolute),
        OpCode::new(0x9d, "STA", 5, AddressingMode::AbsoluteX),
        OpCode::new(0x99, "STA", 5, AddressingMode::AbsoluteY),
        OpCode::new(0x81, "STA", 6, AddressingMode::IndirectX),
        OpCode::new(0x91, "STA", 6, AddressingMode::IndirectY),
        // STX
        OpCode::new(0x86, "STX", 3, AddressingMode::ZeroPage),
        OpCode::new(0x96, "STX", 4, AddressingMode::ZeroPageY),
        OpCode::new(0x8e, "STX", 4, AddressingMode::Absolute),
        // STY
        OpCode::new(0x84, "STY", 3, AddressingMode::ZeroPage),
        OpCode::new(0x94, "STY", 4, AddressingMode::ZeroPageX),
        OpCode::new(0x8c, "STY", 4, AddressingMode::Absolute),
        //
        OpCode::new(0xaa, "TAX", 2, AddressingMode::NoneAddressing),
        OpCode::new(0xa8, "TAY", 2, AddressingMode::NoneAddressing),
        OpCode::new(0xba, "TSX", 2, AddressingMode::NoneAddressing),
        OpCode::new(0x8a, "TXA", 2, AddressingMode::NoneAddressing),
        OpCode::new(0x9a, "TXS", 2, AddressingMode::NoneAddressing),
        OpCode::new(0x98, "TYA", 2, AddressingMode::NoneAddressing),
    ];
    pub static ref OPCODES_MAP: HashMap<u8, &'static OpCode> = {
        let mut map = HashMap::new();
        for opcode in &*CPU_OPS_CODES {
            map.insert(opcode.code, opcode);
        }
        map
    };
}
