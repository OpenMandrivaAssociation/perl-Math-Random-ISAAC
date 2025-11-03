%define module Math-Random-ISAAC
%undefine _debugsource_packages

Name:		perl-%{module}
Version:	1.004
Release:	1
Summary:	Pseufo-Random Number Generator algorith
URL:		https://metacpan.org/pod/Math::Random::ISAAC
Source:		https://cpan.org/modules/by-module/Math/%{module}-%{version}.tar.gz
License:	Perl (Artistic or GPL)
Group:		Development/Perl
BuildArch:	noarch

BuildRequires:	perl
BuildRequires:	perl(Test::NoWarnings)

%description
As with other Pseudo-Random Number Generator (PRNG) algorithms like the Mersenne Twister (see Math::Random::MT), this algorithm is designed to take some seed information and produce seemingly random results as output.

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/*/*
%{_mandir}/man3/*.3pm*
