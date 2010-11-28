Name:		extundelete
Version:	0.2.0
Release:	%mkrel 1
Summary:	Investigation and recovery tool for ext3/4 filesystem
Group:		File tools
License:	GPLv2+
URL:		http://extundelete.sourceforge.net/
Source:		http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	ext2fs-devel

%description
Extundelete is a utility to undelete files from an ext3 or ext4 partition.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp src/extundelete %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}	

%files
%defattr(-,root,root)
%doc LICENSE README 
%{_bindir}/extundelete

