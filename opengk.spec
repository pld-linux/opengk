Summary:	H.323 basic gatekeeper
Name:		opengk
Version:	1.0.1
Release:	3mdk
License:	MPL
Group:		Communications
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.bz2
Patch0:		%{name}-mak_files.patch.bz2
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.6.1
Requires:	openh323_1 >= 1.6.1
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a very basic H.323 Gatekeeper.

Basic features
---------------
OpenGatekeeper supports all the basic features of an H.323 Gatekeeper such
as registration, admissions and access control, address translation and 
bandwidth monitoring and control.

Advanced features
-----------------
- Gatekeeper routed calls 
- Support of H.323v2 alias types 
  (party number, URL, transport id and email address) 
- Support for gateway prefixes 
- Registration and call activity logs 
- Neighbour gatekeeper database 
- Registration time to live 

%prep
%setup -qn %{name}
%patch0 -p1

%build
PWLIBDIR=%{_prefix}; export PWLIBDIR
OPENH323DIR=%{_prefix}; export OPENH323DIR
make  optshared OPTCCFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install obj_*/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/*

%changelog
* Wed Sep 12 2001 Florin <florin@mandrakesoft.com> 1.0.1-3mdk
- recompile with the new openh323_1

* Thu Aug 23 2001 Florin <florin@mandrakesoft.com> 1.0.1-2mdk
- better description

* Wed Aug 22 2001 Florin <florin@mandrakesoft.com> 1.0.1-1mdk
- new spec
