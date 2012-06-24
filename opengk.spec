Summary:	H.323 basic gatekeeper
Summary(pl):	Podstawowy gatekeeper H.323
Name:		opengk
Version:	1.3.4
Release:	1
License:	MPL
Group:		Networking/Daemons
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
# Source0-md5:	c267eede3519198eb3cd002a2b1ee35d
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.11.5
BuildRequires:	pwlib-devel >= 1.4.9
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very basic H.323 Gatekeeper.

Basic features OpenGatekeeper supports all the basic features of an
H.323 Gatekeeper such as registration, admissions and access control,
address translation and bandwidth monitoring and control.

Advanced features:
- Gatekeeper routed calls
- Support of H.323v2 alias types (party number, URL, transport id and
  email address)
- Support for gateway prefixes
- Registration and call activity logs
- Neighbour gatekeeper database
- Registration time to live

%description -l pl
To jest podstawowy Gatekeeper H.323.

OpenGatekeeper obs�uguje podstwowe mo�liwo�ci Gatekeepera H.323, takie
jak rejestracja, przyjmowanie, kontrola dost�pu, t�umaczenie adres�w,
monitorowanie i kontrola pasma.

Zaawansowane mo�liwo�ci:
- routowane po��czenia
- wsparcie dla typ�w alias�w H.323v2 (numer, URL, transport id, adres
  e-mail)
- obs�uga przedrostk�w bramek
- logowanie rejestracji i po��cze�
- baza danych s�siednich gatekeeper�w
- czas obowi�zywania rejestracji.

%prep
%setup -qn %{name}
%patch0 -p1

%build
PWLIBDIR=%{_prefix}; export PWLIBDIR
OPENH323DIR=%{_prefix}; export OPENH323DIR

%{__make} %{?debug:debug}%{!?debug:opt}shared \
	OPTCCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install obj_*/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
