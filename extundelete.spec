Name:		extundelete
Version:	0.1.8
Release:	%mkrel 1
Summary:	Investigation and recovery tool for ext3/4 filesystem
Group:		File tools
License:	GPLv2+
URL:		http://extundelete.sourceforge.net/
Source:		http://downloads.sourceforge.net/project/extundelete/extundelete/%{version}/extundelete-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	ext2fs-devel

%description
Extundelete is a utility to undelete files from an ext3 or ext4 partition.

%prep
%setup -q

%build
cd ./src

%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp src/extundelete %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}rpm	

%files
%defattr(-,root,root)
%doc LICENSE README testing.txt
%{_bindir}/extundelete

