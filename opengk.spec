Summary:	H.323 basic gatekeeper
Summary(pl):	Podstawowy gatekeeper H.323
Name:		opengk
Version:	1.13.4
%define fver	%(echo %{version} | tr . _)
Release:	2
License:	MPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/openh323/%{name}-v%{fver}-src.tar.gz
# Source0-md5:	8a7f8a2f61ac4f8011568e874c9fbcca
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.13.4-3
BuildRequires:	pwlib-devel >= 1.6.5-3
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

OpenGatekeeper obs�uguje podstawowe mo�liwo�ci Gatekeepera H.323, takie
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
