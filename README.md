# Binary Maze CTF Challenge - Official Writeup

## Challenge Description

**Title**: Binary Maze

**Category**: Reverse Engineering

**Difficulty**: Hard

**Points**: 500

**Author**: [Evil0ctal](https://github.com/Evil0ctal/Binary-Maze-CTF-Challenge)

**Files**: 
- binary_maze (encrypted binary)
- binary_maze.iv (initialization vector)
- source.py (obfuscated source code)

### Description
A mysterious program has been discovered, heavily protected and obfuscated. Your mission is to navigate through multiple layers of protection, understand the internal virtual machine, and ultimately extract the flag. Be warned - what you see might not be what you get.

## Technical Overview

The challenge consists of multiple layers of protection:

1. Code Protection Layers:
   - Anti-debugging mechanisms
   - Self-modifying code
   - Control flow obfuscation
   - Custom virtual machine
   - Hardware-bound encryption

2. Obfuscation Techniques:
   - Mixed Boolean-Arithmetic (MBA) expressions
   - Control flow flattening
   - Instruction virtualization
   - Metamorphic code generation
   - Opaque predicates

## Step-by-Step Solution

### Stage 1: Initial Analysis

First, we need to understand the basic structure of the obfuscated code:

```python
# Initial obfuscated code snippet
(lambda τ,π,μ,ρ,σ:exec(τ(π(μ(''.join([chr(ord(c)^42)for c in"¦´±¤¨¶·²¥­¶¶®¯¥¤´±¤¶·¦²¨±·§´±¦¨¸±¦·¦´±¨¥¥²¶·§´±¸·²µ¦¶°¦¶£¬®¬¨¶¸¦µ"])))))))(eval,''.join,list,chr,ord)
```

Key observations:
1. Uses lambda functions for code generation
2. Multiple layers of character encoding
3. XOR operations with key 42

### Stage 2: Deobfuscation

To deobfuscate the code, we need to:

1. Create a deobfuscation script:
```python
def deobfuscate_layer1(code):
    return ''.join([chr(ord(c)^42) for c in code])

def decode_base64_custom(encoded):
    return base64.b64decode(''.join([chr(ord(c)^0x17) for c in encoded]))
```

2. Handle the Greek letter variables:
```python
# Variable mapping
τ = eval
π = ''.join
μ = list
ρ = chr
σ = ord
```

### Stage 3: Virtual Machine Analysis

The challenge uses a custom VM with:

1. Register set:
```python
class SelfModifyingVM:
    def __init__(self):
        self.registers = [0] * 16
        self.memory = mmap.mmap(-1, 4096)
        self.pc = 0
```

2. Instruction set:
- XOR with rotation
- Custom arithmetic
- Control flow manipulation

### Stage 4: Anti-Debug Bypass

Several anti-debugging techniques need to be bypassed:

1. Time-based detection:
```python
def detect_debugger():
    start = time.time()
    time.sleep(0.1)
    elapsed = time.time() - start
    return elapsed < 0.1
```

Solution: Patch the timing checks or use a debugger that can bypass them.

2. Signal handlers:
```python
signal.signal(signal.SIGTRAP, self._handle_trap)
```

Solution: Disable signal handlers or use hardware breakpoints.

### Stage 5: Encryption Analysis

The challenge uses multiple encryption layers:

1. AES-GCM encryption
2. Custom rolling XOR
3. Polymorphic encoding

Key insights:
- The encryption key is hardware-bound
- Multiple layers need to be reversed in order
- Each layer adds its own complexity

### Stage 6: Flag Extraction

The flag is hidden in the code as an XOR-encoded byte array:

```python
ς=b"".join([bytes([x^42])for x in[94,108,97,103,123,77,97,115,55,101,114,95,48,102,95,66,105,110,52,114,121,95,67,104,52,111,115,95,50,48,50,52,125]])
```

To extract the flag:
1. Extract the byte array
2. XOR each byte with 42
3. Convert to ASCII

Final flag: `flag{Mas7er_0f_Bin4ry_Ch4os_2024}`

## Advanced Protection Analysis

### 1. MBA Obfuscation
Example of MBA transformation:
```python
# Original: x + y
# Transformed: (x ^ y) + 2 * (x & y)
# Further obfuscated: ((x | y) + (x & y)) * ((x ^ y) + 2 * (x & y))
```

### 2. Control Flow Flattening
```python
class ControlFlowFlattening:
    def flatten_code(self, code_blocks):
        state_machine = {}
        dispatch_table = {}
        # Complex state machine implementation
```

### 3. Virtualization Protection
- Custom instruction set
- Dynamic code generation
- State machine based execution

## Lessons Learned

1. Reverse Engineering Skills:
   - Advanced debugging techniques
   - Virtual machine analysis
   - Code deobfuscation
   - Encryption analysis

2. Protection Mechanisms:
   - Multiple layers of obfuscation
   - Anti-debugging techniques
   - Custom virtual machines
   - Hardware binding

3. Problem Solving:
   - Layer-by-layer analysis
   - Pattern recognition
   - Creative thinking

## Tools Used

1. Static Analysis:
   - IDA Pro
   - Ghidra
   - Binary Ninja

2. Dynamic Analysis:
   - x64dbg/WinDbg
   - Python debugger
   - Custom deobfuscation scripts

3. Custom Tools:
   - VM instruction analyzer
   - Deobfuscation framework
   - Pattern matching tools

## Additional Notes

1. Common Pitfalls:
   - Focusing too much on surface-level obfuscation
   - Missing hardware binding checks
   - Overlooking anti-debug techniques

2. Alternative Solutions:
   - Full VM emulation
   - Static analysis with symbolic execution
   - Dynamic binary instrumentation

## Conclusion

This challenge demonstrates advanced binary protection techniques and requires a deep understanding of:
- Reverse engineering
- Virtual machines
- Code obfuscation
- Anti-debugging
- Encryption

Success requires both technical skills and creative problem-solving approaches.

## References

1. Research Papers:
   - "Mixed Boolean-Arithmetic Obfuscation"
   - "Virtual Machine Based Software Protection"
   - "Advanced Anti-Debugging Techniques"

2. Tools Documentation:
   - IDA Pro Manual
   - Ghidra User Guide
   - Python Debugger Documentation

3. Related CTF Challenges:
   - Similar VM-based challenges
   - Anti-debug focused problems
   - Obfuscation challenges

---

*Note: This writeup is intended for educational purposes after the CTF competition has ended.*
