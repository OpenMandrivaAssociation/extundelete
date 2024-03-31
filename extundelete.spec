Name:		extundelete
Version:	0.2.4
Release:	1
Summary:	Investigation and recovery tool for ext3/4 filesystem
Group:		File tools
License:	GPLv2+
URL:		http://extundelete.sourceforge.net/
Source:		http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:		https://src.fedoraproject.org/rpms/extundelete/raw/rawhide/f/extundelete-0.2.4-i_size_high.patch
Patch1:		extundelete-0.2.4-fix-build.patch
BuildRequires:	git-core
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	automake
BuildRequires:	autoconf

%description
Extundelete is a utility to undelete files from an ext3 or ext4 partition.

%prep
%autosetup -p1
%configure

%build
%make_build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp src/extundelete %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%doc LICENSE README 
%{_bindir}/extundelete
