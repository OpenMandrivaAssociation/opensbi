# This is intentional, since OpenSBI is needed to emulate
# full RISC-V platforms with qemu
%define _binaries_in_noarch_packages_terminate_build 0

# Doesn't go well with noarch
%define __find_debuginfo %{_bindir}/true

Name:		opensbi
Version:	1.4
Release:	1
Summary:	RISC-V OpenSBI Development file
License:	BSD-2-Clause
Group:		Development/Other
Url:		https://github.com/riscv/opensbi
BuildRequires:	python >= 3.0
Source:		https://codeload.github.com/riscv-software-src/opensbi/tar.gz/refs/tags/v1.4#/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	cross-riscv64-openmandriva-linux-gnu-binutils
BuildRequires:	cross-riscv64-openmandriva-linux-gnu-gcc

%description
The goal of the OpenSBI project is to provide an open-source reference
implementation of the RISC-V SBI specifications for platform-specific
firmwares executing in M-mode (case 1 mentioned above). An OpenSBI
implementation can be easily extended by RISC-V platform and
system-on-chip vendors to fit a particular hardware configuration.

%prep
%autosetup -p1

%build
%make_build V=1 O=build PLATFORM=generic FW_PIC=y CROSS_COMPILE=riscv64-openmandriva-linux-gnu-

%install
make install O=build I=%buildroot PLATFORM=generic \
     INSTALL_FIRMWARE_PATH=%_datadir/opensbi \
     INSTALL_INCLUDE_PATH=%_includedir \
     INSTALL_LIB_PATH=%_libdir

rm -vfr \
    %buildroot%_datadir/opensbi/generic/firmware/payloads \
    %buildroot%_includedir \
    %buildroot%_libdir

%files
%doc README.md CONTRIBUTORS.md COPYING.BSD
%_datadir/opensbi/generic/firmware
