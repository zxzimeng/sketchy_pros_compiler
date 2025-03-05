# Sketchy PROS Compiler Wrapper

A build system wrapper for PROS robotics projects that provides file change tracking, build logging, and binary backups.

# Installation

Install from PyPI:

```bash
pip install sketchy-pros-compiler
```

Install from git
```bash
git clone https://github.com/zxzimeng/sketchy_pros_compiler.git
cd sketchy_pros_compiler
pip install .
```

## Features

- Tracks changes between compilations
- Concatenates source files for faster compilation
- Preserves original file structure
- Maintains build history with timestamps
- Backs up binary files after successful builds
- Diff output for file changes to see the changes made since last compile

## Performance Benefits

### Standard PROS Build
```bash
$time pros --no-analytics make  
> 21.58s user 1.90s system 98% cpu 23.819 total

$ls -s bin/hot.package.elf
Binary size: 9064KB (bin/hot.package.elf)
```

### Sketchy PROS Compiler
```bash
$time sketchy_pros_compiler
> 2.77s user 0.47s system 85% cpu 3.769 total

$ls -s bin/hot.package.elf
Binary size: 6728KB (bin/hot.package.elf)
```

**Improvements:**
- Faster compilation, smaller compiliation size on larger projects
- Maintains full functionality, file structure, and readability
- Includes change tracking and backup features

## Directory Structure

```plaintext
~/tmp/sketchycompiler/
├── hard/                     # Temporary build files
├── softstorage/             # Source file snapshots for diff comparison
└── logstorage/             
    ├── build_history.log    # Complete build history
    └── [timestamp]/         # Per-build archives
        ├── changes.log      # File changes for this build
        └── bin/*            # Binary backup from this build
```

## Usage

After installing to path, run from within a PROS project directory to build:

```bash
pros_sketchy
```

The script will:
1. Show changes since last compilation
2. Concatenate source files (excluding auton_selector)
3. Run PROS build system
4. Restore original file structure
5. Archive build artifacts and changes

## Requirements

- PROS CLI installed and configured
- macOS environment

## Sample Run Output

```ansi
❯ pros_sketchy 
[34m=== Changes since last compilation ===[0m

[36m=== File: auton_programs/blue_right.cpp ===[0m
@@ -11,7 +11,7 @@

         // Get First Mogo
         chassis.processMovement(Movement{
-                                    .pose = {-41.652, -36.117, 270}, .offset_distance = 0, .perp_offset_distance = 0,
+                                    .pose = {-43, -5, 270}, .offset_distance = 0, .perp_offset_distance = 0,
                                     .moveParams = MoveToPoseParams{.forwards = false, .minSpeed = 70},
                                     .exitDistance = 0,
                                     .timeout = 4000

[35m════════════════════════════════════════════════════════════════[0m
[36m                      PROS Build Output                           [0m
[35m════════════════════════════════════════════════════════════════[0m

Compiled src/main.cpp [WARNINGS]
src/main.cpp: In member function 'void Aux::watchIndexer()':
src/main.cpp:2321:23: warning: comparison between 'enum Aux::ConveyorState' and 'enum Aux::IntakeClawSystemState' [-Wenum-compare]
 2321 |     if (conveyorState == AUTO_CONVEYOR) {
      |         ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~
In file included from ./include/lemlib/api.hpp:5,
                 from ./include/main.h:43,
                 from src/main.cpp:1:
./include/lemlib/util.hpp: At global scope:
./include/lemlib/util.hpp:78:17: warning: inline function 'constexpr float lemlib::sanitizeAngle(float, bool)' used but never defined
   78 | constexpr float sanitizeAngle(float angle, bool radians = true);
      |                 ^~~~~~~~~~~~~
Adding timestamp [OK]
Linking hot project with ./bin/cold.package.elf and LemLib,libc,liblvgl,libm,libpros [OK]
Section sizes:
   text	  data	   bss	 total	   hex	filename
  97356	    20	48249600	48346976	2e1b760	bin/hot.package.elf
Creating bin/hot.package.bin for VEX EDR V5 [DONE]
Compilation complete and files restored successfully.

[35m════════════════════════════════════════════════════════════════[0m
[36m                      Final File Status                           [0m
[35m════════════════════════════════════════════════════════════════[0m

[34m=== Changes since last compilation ===[0m
[33mNo changes detected in any files[0m
```

## Build Archives

Each build creates a timestamped directory containing:
- Binary files from successful builds
- Detailed change logs
- Compilation status and warnings
- Full build output history

Access previous builds in `~/tmp/sketchycompiler/logstorage/`

## How It Works

1. **Change Detection**
   - Tracks file modifications between builds
   - Shows colorized diffs of changes
   - Maintains history of all modifications

2. **Build Optimization**
   - Concatenates source files for faster compilation
   - Reduces binary size through optimized linking
   - Preserves original project structure

3. **Backup System**
   - Archives each build with timestamp
   - Stores binary files and changes
   - Maintains complete build history

4. **File Management**
   - Temporary build directory for compilation
   - Automatic restoration of original files
   - Structured storage of build artifacts

## Limitations

You may not use the same variable names for the variables in different files as they will be compiled in one file,
variable hashing is not supported yet.