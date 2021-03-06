%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-JSON-PP
Version:        2.97001
Release:        1%{?dist}
Summary:        JSON::XS compatible pure-Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/JSON-PP/
Source0:        http://www.planet-elektronik.de/CPAN//authors/id/I/IS/ISHIGAKI/JSON-PP-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util) >= 1.08
BuildRequires:  perl(Test::More)
Requires:       perl(Scalar::Util) >= 1.08
Requires:       perl(Test::More)

%description
JSON::PP is a pure perl JSON decoder/encoder (as of RFC4627, which we know
is obsolete but we still stick to; see below for an option to support part
of RFC7159), and (almost) compatible to much faster JSON::XS written by
Marc Lehmann in C. JSON::PP works as a fallback module when you use JSON
module without having installed JSON::XS.

%prep
%setup -q -n JSON-PP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 2.97001-1
- Specfile autogenerated by cpanspec 1.78.
